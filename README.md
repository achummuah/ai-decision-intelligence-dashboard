\# AI Decision Intelligence Dashboard



Automated Revenue Risk Monitoring \& Business Decision Support System



---



\## 📌 Overview



AI Decision Intelligence Dashboard is a Python-based automation tool that analyzes business transaction data to identify operational risks, estimate potential revenue loss, and automatically generate an executive-ready Excel dashboard.



Instead of manually analyzing reports, businesses can run a single script to obtain actionable insights and a fully prepared management dashboard.



---



\## 🎯 Problem



Businesses frequently lose revenue due to:



\- Payment failures

\- Delivery delays

\- Stock unavailability

\- High-value risky transactions



Traditional monitoring methods are reactive and require manual reporting.



This project introduces an automated \*\*Decision Intelligence System\*\* that proactively detects risks and recommends corrective actions.



---



\## 🧠 Solution



The system performs an end-to-end analytics workflow:



1\. Data cleaning and preprocessing

2\. Feature engineering

3\. Risk scoring using weighted business rules

4\. Risk classification (Low / Medium)

5\. Revenue loss prediction

6\. Automated intervention suggestions

7\. Automatic Excel dashboard generation with charts



No manual Excel work is required.



---



\## ⚙️ Tech Stack



\- Python 3.x

\- Pandas

\- NumPy

\- XlsxWriter (Excel automation \& charts)

\- Microsoft Excel (Dashboard output)



---



\## ✨ Features



\- Automated dataset cleaning

\- AI-style weighted risk scoring

\- Transaction risk classification

\- Predicted revenue loss estimation

\- Automated intervention recommendations

\- Revenue recovery simulation

\- Self-generating Excel dashboard

\- Automatic chart creation via Python



---



\## 🏗️ System Architecture

Raw Dataset

↓

Data Cleaning \& Processing

↓

Risk Scoring Engine

↓

Revenue Loss Prediction

↓

Intervention Recommendation Engine

↓

Automated Excel Dashboard Generation





---



\## 📂 Project Structure





team\_biztrack/

│

├── ai\_decision\_pipeline.py # Main executable script

├── sample\_dataset.xlsx # Example dataset

├── requirements.txt # Dependencies

├── README.md

├── LICENSE

└── .gitignore





---



\## 📦 Installation



Clone the repository:



```bash

git clone <repository-link>

cd team\_biztrack



Install dependencies:



pip install -r requirements.txt

▶️ How to Run



Make sure the dataset file exists in the project folder:



sample\_dataset.xlsx



Run the script:



python ai\_decision\_pipeline.py

📊 Output



After execution, the system automatically generates:



AI\_Decision\_Intelligence\_Report.xlsx



The Excel file contains:



Executive KPI summary



Risk monitoring dashboard



Revenue impact charts



Automated intervention analysis



Processed transaction data



All charts are generated automatically — no manual dashboard creation required.



💻 Usage Examples

Example 1 — Basic Execution

python ai\_decision\_pipeline.py



Output:



✅ Fully Automated AI Dashboard Generated

Example 2 — Business Scenario



Input conditions:



Failed payments detected



Delivery delays present



Stock shortages recorded



System output:



Risk classification for orders



Predicted revenue loss



Suggested recovery actions



Executive dashboard automatically generated



Example 3 — Using Another Dataset



Replace:



sample\_dataset.xlsx



with another transaction dataset and update the filename inside the script.



Run again:



python ai\_decision\_pipeline.py

🔍 Risk Scoring Model



The system calculates risk using weighted business logic:



Condition	Weight

Payment failure	+40

Stock unavailable	+35

Delivery delay	+25

High-value order (>5000)	+20

Risk Levels



0–39 → Low Risk



40–79 → Medium Risk



80+ → High Risk



Predicted Revenue Loss

Predicted Loss = Risk Score × Order Value

📈 Dashboard Insights



Generated dashboard includes:



Risk distribution visualization



Financial risk impact analysis



Automated intervention tracking



Executive performance metrics



👥 Team Members



Member 1 — Ayushi Singh - Data Analysis and Dashboard Preparation



Member 2 — Archana Amit Naik - Code writing



🤖 AI Assistance Disclosure



AI tools (ChatGPT, eraser.io)were used for:
Flowchart making


Documentation structuring



Architecture planning



Automation guidance



All implementation and validation were completed manually by the team.



📄 License



This project is licensed under the MIT License.



🎥 Demo Video



https://drive.google.com/file/d/17hRPHFcWsvNW2FM1a-0T8eX5If9rw1U4/view?usp=sharing



❤️ Built by team biztrack for TinkerHub Hackathon

