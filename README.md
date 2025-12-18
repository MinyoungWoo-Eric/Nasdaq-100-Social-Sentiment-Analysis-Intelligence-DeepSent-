# DeepSent（2025）: *Nasdaq-100 Social Sentiment Analysis Intelligence*
View in Streamlit: https://deepsent2025.streamlit.app/

---

- **Authors**: *Lechuan Wang, Minyoung Woo, Xuantao Yuan, Yijie Wang*
- **Institution**: Hong Kong University of Science and Technology, MSc in Business Analytics
- **Correspondence**: lechuanwang2003@163.com

## Example Output
### *Part 1: Fundamental Data Sector*
<img width="1126" height="1100" alt="d50cf9c14377d9d46c40b0e632a5f13a" src="https://github.com/user-attachments/assets/ebd2fbed-a875-4eda-8549-8859708abb0b" />

### *Part 2: Sentiment Analysis Report Generator*
<img width="1102" height="328" alt="7c56b2690a8bef945027e21add83c508" src="https://github.com/user-attachments/assets/461679f3-1dc1-4303-a037-9db04a8cf363" />

### *Part 3: Report Content (Taking Nvidia's December 2nd to December 9th as an example)*
#### *The report contains Snapshot & Trend Sector, `Sentiment Anomaly Drivers` Analysis, `Bull vs Bear Narrative Dominance`, `Short-Term Price Implication`, and `Daily Event Timeline` sections.*
<img width="1706" height="288" alt="038a961020d09a7154336a933e16ae18" src="https://github.com/user-attachments/assets/d0a8a53b-6c98-40a6-86ee-cbd05791a7ed" />
<img width="1462" height="1620" alt="3a00ef792e4fc988cff61d327712629d" src="https://github.com/user-attachments/assets/c8d94679-a63d-4a15-875f-a949e46ef725" />

<img width="1458" height="464" alt="fb68696e30dee46046f9fe1808471b51" src="https://github.com/user-attachments/assets/8f0bddf4-a902-4225-ac8f-f4dcd12550c4" />
<img width="1600" height="744" alt="9ad7427ecabc735a1b72c2619dac2e93" src="https://github.com/user-attachments/assets/42a59c74-41ac-4d92-9444-d31a0576d691" />

<img width="1598" height="1302" alt="f4b0020058fe8ae7c104feba0d958793" src="https://github.com/user-attachments/assets/d9ff2c53-1a5a-4ed0-a602-cff24c47ba2a" />

<img width="1586" height="284" alt="4e2533dd937f3bff86e744135208b0e7" src="https://github.com/user-attachments/assets/1286f8ce-a74f-48f3-aa0e-e34a86afc157" />
<img width="1598" height="326" alt="d5611238cce6b5f692b96274875194e1" src="https://github.com/user-attachments/assets/ca8a038e-1023-4609-94ee-98ff1ea14810" />

<img width="1586" height="1642" alt="476145f0831e66e10d63402138931427" src="https://github.com/user-attachments/assets/8afd0a99-2754-4593-9cd5-4421f5004c20" />
<img width="1590" height="370" alt="24dd35945ef0114c18d52e853ca0d6e9" src="https://github.com/user-attachments/assets/c0708a61-f8e0-4c3f-beed-8fff53ec2e81" />
<img width="1588" height="1182" alt="4a21eb5a43f2fad4fb99625d7bad4f43" src="https://github.com/user-attachments/assets/037a8325-7ce8-4c6a-83f6-bd118e2248cb" />
<img width="1598" height="1132" alt="bd0a7d703d9589f6d07a9dea8172043c" src="https://github.com/user-attachments/assets/3e6de884-d8d6-4cbe-bbbd-06f0b85d6313" />
<img width="1600" height="626" alt="1ed4d91d78261ba747d1618b4e2ba7b6" src="https://github.com/user-attachments/assets/e824e312-d17d-484f-938d-882cb4be6d83" />


# Our Purpose
## 1. Traditional Challenge: Information Overload
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


## 4. Intended Users & Use Cases
| User Type | Core Use Cases |
|-----------|----------------|
| Portfolio Managers | Early sentiment signals for timing, position sizing, and risk alerts |
| Equity Researchers | Faster, richer market-color narratives for client conversations |
| Risk & Compliance | Sentiment shock detection and audit-ready monitoring logs |
| Individual Active Traders / Investors | Professional-grade sentiment analysis for personal portfolio decisions (no need to build own infrastructure) |


## 5. System Architecture: Multi-Staged AI Agent

<img width="2660" height="1108" alt="3a2a280ce34caa19c5a29d71c553f056" src="https://github.com/user-attachments/assets/ed422849-bcfd-4241-ab2c-dc111e1e2fd8" />


## 6. Governance & Responsible AI Design
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


## 7. Technology: Availability of Core Components
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
