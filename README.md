# DeepSent: Nasdaq-100 Social Sentiment Analysis Intelligence

## Project Overview
- **Authorss**: Lechuan Wang, Minyoung Woo, Yijie Wang, Xuantao Yuan
- **Institution**: Hong Kong University of Science and Technology, MSc in Business Analytics
- **Core Purpose**: AI-powered sentiment analysis tool for Nasdaq-100 stocks, addressing information overload in financial decision-making

---

## 1. The Challenge: Information Overload
### Traditional Manual Analysis Pain Points
- Scattered Information
- Time-Consuming
- No Consistency
- Shallow Insights

### Consequences
- ⏱️ Delayed Decisions
- 🚨 Missed Signals
- 📋 Audit Gaps
- 😕 Low Confidence

---

## 2. Solution: Sentiment Analysis Report
### Key Features
#### Single-Channel Reliability
- Alpha Vantage curated financial news
- Quality over quantity – eliminate social media noise

#### Customizable Parameters (User Control)
- Number of Articles per Day
- Time Window

#### Deep AI Insights (Powered by GPT-4o)
- Root Cause Analysis
- Theme Extraction
- Anomaly Detection
- Short-term Implication
- Event Timeline

#### Professional Export
- Download as markdown format
- Includes charts, indicators, narratives, and timeline

---

## 3. Potential Impact & Strategic Value
### 🔍 Analysis Depth
- Not a single sentiment score
- Combine Score + Root Cause + Themes (with source)
- Root cause analysis distinguishes signal from noise
- Improve confidence in decisions

### 🛡️ Better Risk Management
- Proactive identification of sentiment-driven risks
- Data-backed risk assessment

### ✓ Reliability
- All insights source-anchored
- Zero hallucination through RAG technology
- Build confidence through transparency

### ⏳ Massive Time Savings
- Spend less time collecting & summarizing data
- More time on judgement & strategy development

---

## 4. Intended Users & Use Cases
| User Type | Core Use Cases |
|-----------|----------------|
| Portfolio Managers | Early sentiment signals for timing, position sizing, and risk alerts |
| Equity Researchers | Faster, richer market-color narratives for client conversations |
| Risk & Compliance | Sentiment shock detection and audit-ready monitoring logs |
| Individual Active Traders / Investors | Professional-grade sentiment analysis for personal portfolio decisions (no need to build own infrastructure) |

---

## 5. Live Demo: What You'll See
1. **Select Stock**: Choose a Nasdaq-100 ticker (e.g., NVDA, TSLA)
2. **Price & Fundamentals**:
   - Price & Volume Chart (customizable Time Period)
   - Core Trading Indicators
3. **AI Reports Configuration**: Users choose number of articles/day + time window
4. **Key Insights**:
   - Sentiment Trends
   - Sentiment Anomaly Drivers (Root Cause Analysis)
   - Bull & Bear Narrative Dominance
   - Short-Term Implication
5. **Appendix**: Daily Event Timeline – Quickly understand market context

---

## 6. System Architecture: Multi-Staged AI Agent

<img width="2066" height="852" alt="ad78cc629d766fcfcc0cb995dc787065" src="https://github.com/user-attachments/assets/50cc2638-2e26-4be0-b638-e24483c77786" />

---

## 7. Governance & Responsible AI Design
### 🔐 Data Governance
- Public data only (Alpha Vantage & Yahoo Finance)
- Source transparency
- No personal data collection

### 🔍 AI Transparency
- Show articles (with source evidence) behind sentiment scores
- RAG-anchored narratives (no hallucinations)

### 👤 Human-in-the-Loop
- Decision-support tool only
- No autonomous trading functionality
- Sentiment as one signal among many (not sole decision driver)

### ⚖️ Regulatory Alignment
- Positioned as research tool, not investment advice
- Audit-ready design for compliance requirements

---

## 8. Technology: Availability of Core Components
| Component | Technology Used | Key Capabilities |
|-----------|-----------------|------------------|
| Interface | Streamlit | Rapid construction of interactive interfaces (stock search + data display + report generation) |
| Data Collection | Alpha Vantage | Reliable financial news + sentiment data |
| Data Collection | Yahoo Finance | Core trading indicators, price/volume information |
| Sentiment Processing | RAG Technology | Efficiently retrieve and integrate multi-source sentiment text; solve "limited content quality per API call" issue |
| AI Report Generation | GPT-4o | Professional financial analysis capabilities; support multi-round calls to compile in-depth long reports |

---

## Disclaimer
- DeepSent is a research tool for decision support, not a substitute for professional investment advice.
- All investment decisions should be made after comprehensive analysis and consideration of personal risk tolerance.
