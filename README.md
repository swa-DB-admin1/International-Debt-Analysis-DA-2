# International-Debt-Analysis-DA-2

Overview

International Debt Analytics is a data analytics mini project that analyzes global debt data using Python, MySQL, SQL, Pandas, Streamlit, and Plotly. The project transforms cleaned CSV data into a structured MySQL database, performs 30 SQL-based analytical queries, and presents the results through an interactive dashboard.

🎯 Key Insights

The dashboard focuses on:

🌍 Country-wise debt distribution
🏆 Top and lowest debt countries
📊 Debt distribution across different indicators
📈 International debt trends and patterns
🔎 Interactive analysis using Country, Indicator, and Year filters
💡 Data-driven decision making

🔄 Project Workflow

5 Cleaned CSV Files
        ↓
MySQL Database
        ↓
5 Related Tables
        ↓
Primary Keys & Foreign Keys
        ↓
30 SQL Analytical Questions
        ↓
queries.py
        ↓
Streamlit + Plotly Dashboard
        ↓
Interactive Debt Insights



🛠️ Technologies Used
Python – Data processing and application development
Pandas – Data cleaning and analysis
MySQL – Database storage
SQL – Data analysis and business questions
Streamlit – Interactive dashboard
Plotly – Data visualization
Jupyter Notebook – Data exploration
GitHub – Version control


📊 Dashboard

The Streamlit dashboard provides:

Total Debt
Number of Countries
Number of Indicators
Number of Years
Top countries by debt
Lowest debt countries
Debt distribution
Indicator analysis
Year-wise debt trends
Interactive filters

Various visualizations such as bar charts, line charts, donut charts, and comparison charts are used to make the analysis easy to understand.

🗄️ Database & SQL Analysis

The cleaned datasets are stored in a MySQL database named:
international_debt


The database contains 5 related tables connected using primary and foreign keys.

A total of 30 SQL questions were created to analyze country-level debt, indicators, trends, rankings, and comparisons. The queries are maintained in:

app/queries.py
📁 Project Structure
International_Debt_Analytics_DA2/
│
├── app/
│   ├── db_connection.py
│   ├── queries.py
│   └── __init__.py
│
├── data/
│   └── cleaned CSV files
│
├── notebooks/
│   └── data_analysis.ipynb
│
├── dashboard.py
├── requirements.txt
├── .gitignore
└── README.md
▶️ Run the Project

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure the MySQL connection in app/db_connection.py, then run:

python -m streamlit run dashboard.py

The dashboard will be available at:

http://localhost:8501
💡 Project Outcome

This project demonstrates an end-to-end analytics workflow, from data cleaning and relational database design to SQL analysis and interactive visualization, providing meaningful insights into international debt and supporting data-driven decision making.

👩‍💻 Author

Swathi Sri K S
