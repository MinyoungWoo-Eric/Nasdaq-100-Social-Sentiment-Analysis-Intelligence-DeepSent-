# stock_basic_data.py
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import talib
import warnings
import requests

warnings.filterwarnings("ignore")

# ======================== 实时 Nasdaq-100 列表（启动时只抓一次 Ticker 列表） ========================
def _fetch_nasdaq100_tickers():
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/Nasdaq-100")
        df = tables[4]
        tickers = df["Ticker"].str.replace(".", "-").tolist()
        return sorted(tickers)
    except:
        return [
            "AAPL","MSFT","NVDA","GOOGL","AMZN","META","AVGO","GOOG","TSLA","LLY",
            "JPM","UNH","XOM","V","MA","PG","JNJ","HD","COST","MRK","ABBV","CRM",
            "NFLX","BAC","AMD","CVX","KO","ADBE","PEP","TMO","LIN","WMT","ACN",
            "CSCO","MCD","ABT","TXN","QCOM","INTU","AMGN","VZ","PFE","IBM","CMCSA",
            "DIS","NOW","RTX","SPGI","UNP","ISRG","GE","CAT","BKNG","UBER","GS",
            "NEE","PM","MS","LOW","BLK","HON","SYK","ELV","TJX","VRTX","BSX","LRCX",
            "REGN","ETN","PLD","MDT","MU","PANW","ADP","KLAC","LMT","CB","ADI","DE",
            "MMC","ANET","SCHW","FI","BX","MDLZ","TMUS","AMT","SO","BMY","MO","GILD",
            "CL","ICE","CME","DUK","ZTS","SHW","TT","MCO","CVS","BN","EOG","ITW",
            "FCX","TGT","BDX","CSX","HCA","EMR","FDX","NOC"
        ]

NASDAQ100_TICKERS = _fetch_nasdaq100_tickers()

STOCK_TICKERS = NASDAQ100_TICKERS
STOCK_FULL_NAMES = {}  

def get_company_name(ticker: str) -> str:
    """实时获取公司全名（用户点哪只再请求，秒开）"""
    if ticker in STOCK_FULL_NAMES:
        return STOCK_FULL_NAMES[ticker]
    try:
        info = yf.Ticker(ticker).info
        name = info.get("longName", ticker)
        STOCK_FULL_NAMES[ticker] = name
        return name
    except:
        return ticker

TIME_PERIODS = {
    "1 Month":  "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year":   "1y"
}

# ======================== 其余代码完全不动（指标、图表函数等） ========================

def get_stock_price_data(ticker, period="1y", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    hist.reset_index(inplace=True)
    hist["Date"] = hist["Date"].dt.strftime("%Y-%m-%d")
    hist = hist.dropna()
    return hist

def get_stock_fundamental_data(ticker):
    stock = yf.Ticker(ticker)
    price_data = get_stock_price_data(ticker, period="1y")
    
    tech_indicators = {}
    if not price_data.empty and len(price_data) >= 60:
        tech_indicators["5D Change (%)"] = round(((price_data["Close"].iloc[-1] / price_data["Close"].iloc[-5]) - 1) * 100, 2)
        tech_indicators["60D Change (%)"] = round(((price_data["Close"].iloc[-1] / price_data["Close"].iloc[-60]) - 1) * 100, 2)
        
        close_prices = price_data["Close"].values
        rsi = talib.RSI(close_prices, timeperiod=14)
        tech_indicators["RSI (14)"] = round(rsi[-1], 2) if not np.isnan(rsi[-1]) else "N/A"
        
        high = price_data["High"].values
        low = price_data["Low"].values
        atr = talib.ATR(high, low, close_prices, timeperiod=14)
        tech_indicators["ATR (14)"] = round(atr[-1], 2) if not np.isnan(atr[-1]) else "N/A"
    
    # ===== 关键修改：安全获取 info =====
    info = {}
    try:
        info = stock.info or {}  # 如果 info 是 None，直接变空 dict
        if not isinstance(info, dict):
            info = {}
    except Exception:
        info = {}  # 任何异常都兜底为空
    
    fund_indicators = {
        "Gross Margin (%)": round(info.get("grossMargins", 0) * 100, 2) if info.get("grossMargins") is not None else "N/A",
        "ROE (%)": round(info.get("returnOnEquity", 0) * 100, 2) if info.get("returnOnEquity") is not None else "N/A",
        "Forward PE": round(info.get("forwardPE", 0), 2) if info.get("forwardPE") is not None else "N/A",
        "PB Ratio": round(info.get("priceToBook", 0), 2) if info.get("priceToBook") is not None else "N/A",
        "PS Ratio": round(info.get("priceToSalesTrailing12Months", 0), 2) if info.get("priceToSalesTrailing12Months") is not None else "N/A",
    }
    
    all_indicators = {**tech_indicators, **fund_indicators}
    
    # 安全获取公司名和 Sector
    all_indicators["Company Name"] = STOCK_FULL_NAMES.get(ticker, ticker)
    all_indicators["Sector"] = info.get("sector", "N/A")  # 现在安全了，因为 info 一定是 dict
    
    return all_indicators

# ======================== 图表绘制函数（无修改，保留原有） ========================
def plot_ths_style_chart(ticker, df_price, period_label):
    """绘制仿同花顺风格的K线+成交量组合图"""
    if df_price.empty:
        return None, None
    
    # K线图
    fig_kline = go.Figure(data=[go.Candlestick(
        x=df_price["Date"],
        open=df_price["Open"],
        high=df_price["High"],
        low=df_price["Low"],
        close=df_price["Close"],
        name="Price",
        increasing_line_color="#008000",  #FF4500
        decreasing_line_color="#FF4500",  #008000
        showlegend=False
    )])
    
    # 移动平均线
    df_price["MA5"] = df_price["Close"].rolling(window=5).mean()
    df_price["MA10"] = df_price["Close"].rolling(window=10).mean()
    df_price["MA20"] = df_price["Close"].rolling(window=20).mean()
    df_price["MA60"] = df_price["Close"].rolling(window=60).mean()
    
    fig_kline.add_trace(go.Scatter(
        x=df_price["Date"],
        y=df_price["MA5"],
        mode="lines",
        name="MA5",
        line=dict(color="#FFD700", width=1.2),
        showlegend=True
    ))
    fig_kline.add_trace(go.Scatter(
        x=df_price["Date"],
        y=df_price["MA10"],
        mode="lines",
        name="MA10",
        line=dict(color="#FFA500", width=1.2),
        showlegend=True
    ))
    fig_kline.add_trace(go.Scatter(
        x=df_price["Date"],
        y=df_price["MA20"],
        mode="lines",
        name="MA20",
        line=dict(color="#00BFFF", width=1.2),
        showlegend=True
    ))
    fig_kline.add_trace(go.Scatter(
        x=df_price["Date"],
        y=df_price["MA60"],
        mode="lines",
        name="MA60",
        line=dict(color="#9370DB", width=1.2),
        showlegend=True
    ))
    
    # K线图样式
    fig_kline.update_layout(
        title=f"{ticker} Price Chart ({period_label})",
        title_font=dict(size=16, weight="bold", family="Arial"),
        xaxis_title="",
        yaxis_title="Price (USD)",
        template="plotly_white",
        width=1200,
        height=400,
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="right",
            x=1.0,
            font=dict(size=14),
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(0,0,0,0)',
            borderwidth=0
        ),
        margin=dict(l=50, r=20, t=40, b=40)
    )
    fig_kline.update_xaxes(
        rangeslider_visible=False,
        showgrid=True,
        gridcolor="#E6E6E6",
        tickfont=dict(size=10)
    )
    fig_kline.update_yaxes(
        showgrid=True,
        gridcolor="#E6E6E6",
        tickfont=dict(size=10)
    )
    
    # 成交量图
    fig_volume = go.Figure() #FF4500 #008000
    colors = ["#008000" if row["Close"] >= row["Open"] else "#FF4500" for _, row in df_price.iterrows()]
    fig_volume.add_trace(go.Bar(
        x=df_price["Date"],
        y=df_price["Volume"],
        name="Volume",
        marker_color=colors,
        opacity=0.8,
        showlegend=False
    ))
    
    fig_volume.update_layout(
        title=f"{ticker} Volume Chart ({period_label})",
        title_font=dict(size=14, weight="bold", family="Arial"),
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
        width=1200,
        height=200,
        hovermode="x unified",
        margin=dict(l=50, r=20, t=30, b=40),
        font=dict(size=10)
    )
    fig_volume.update_xaxes(
        showgrid=True,
        gridcolor="#E6E6E6",
        tickfont=dict(size=10)
    )
    fig_volume.update_yaxes(
        showgrid=True,
        gridcolor="#E6E6E6",
        tickfont=dict(size=10),
        tickformat=",.0s"
    )
    
    return fig_kline, fig_volume


def plot_sentiment_price_correlation(ticker, price_data, social_data, period_name):
    if len(social_data) < 10:
        return None

    df_posts = pd.DataFrame(social_data)
    df_posts["date"] = pd.to_datetime(df_posts["date_str"])
    
    # 1. 计算每日原始情感分数均值（平滑前）
    daily_raw_sent = df_posts.groupby("date")["sentiment"].mean().reset_index()
    daily_raw_sent.rename(columns={"sentiment": "raw_sentiment"}, inplace=True)
    
    # 2. 计算每日平滑情感分数均值（如果存在smooth_sentiment字段）
    if "smooth_sentiment" in df_posts.columns:
        daily_smooth_sent = df_posts.groupby("date")["smooth_sentiment"].mean().reset_index()
        daily_smooth_sent.rename(columns={"smooth_sentiment": "smooth_sentiment"}, inplace=True)
        # 合并原始+平滑分数
        daily_sent = daily_raw_sent.merge(daily_smooth_sent, on="date", how="inner")
    else:
        # 无平滑分数时，仅保留原始分数
        daily_sent = daily_raw_sent
        daily_sent["smooth_sentiment"] = daily_sent["raw_sentiment"]

    # 合并价格和情绪数据
    price_data["Date"] = pd.to_datetime(price_data["Date"])
    merged = price_data[["Date", "Close"]].merge(daily_sent, left_on="Date", right_on="date", how="left")
    merged = merged.dropna()  # 清除无情绪的日子

    if len(merged) < 10:
        return None

    fig = go.Figure()

    # 3. 绘制股价线（主Y轴）
    fig.add_trace(go.Scatter(
        x=merged["Date"],
        y=merged["Close"],
        mode="lines",
        name="Close Price",
        line=dict(color="#1f77b4", width=3),
        yaxis="y"
    ))

    # 4. 绘制平滑后情感分数（次Y轴，实心圆，绿色）
    fig.add_trace(go.Scatter(
        x=merged["Date"],
        y=merged["smooth_sentiment"],
        mode="markers+lines",  # 带连线，更易看趋势
        name="Smoothed Sentiment",
        marker=dict(size=10, color="#00FF88", opacity=0.8),
        line=dict(color="#00FF88", width=1),
        yaxis="y2"
    ))

    # 5. 绘制原始情感分数（次Y轴，空心圆，橙色，标注在平滑分数旁）
    fig.add_trace(go.Scatter(
        x=merged["Date"],
        y=merged["raw_sentiment"],
        mode="markers",
        name="Raw Sentiment (Pre-smoothing)",
        marker=dict(
            size=8, 
            color="#FF8C00",  # 橙色区分原始分数
            opacity=0.9,
            symbol="circle-open",  # 空心圆样式
            line=dict(color="#FF8C00", width=1)
        ),
        yaxis="y2",
        # 悬停提示补充原始分数值
        hovertemplate="Date: %{x}<br>Raw Sentiment: %{y:.4f}<extra></extra>"
    ))

    # 6. 布局优化
    fig.update_layout(
        title=f"{ticker} — Price vs Sentiment Correlation ({period_name})",
        xaxis_title="Date",
        yaxis=dict(
            title="Price (USD)",
            side="left",
            color="#1f77b4"
        ),
        yaxis2=dict(
            title="Sentiment Score",
            side="right",
            overlaying="y",
            range=[-1.1, 1.1],  # 固定情感分数范围（-1到1）
            color="#00FF88"
        ),
        template="plotly_white",
        hovermode="x unified",
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig
