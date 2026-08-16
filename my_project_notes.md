PART - 1
First create one folder "International_Debt_Analytics-DA2" then crete required folder and files under that


mkdir -p data/raw data/processed notebooks src sql visualizations app

cd notebooks
touch my_project_notes.md 
touch 01_debt_analysis.ipynb

PART -2 Download all CSV files adn move under /data/raw folder

PART -3  Create your Python environment

python3 -m venv venvsource venv/bin/activate
source venv/bin/activate
python --version

PART - 4 Install required python lib

pip install pandas numpy matplotlib seaborn jupyter openpyxl mysql-connector-python sqlalchemy

PART -5 Create your Jupyter Notebook

cd notebooks/


then execute necessary command in notebooks.


SQL INTEGRATION WITH PYTHON

Create one file under app

venv) swathisri.ks@L4T2DYR43N app % touch db_connection.py
(venv) swathisri.ks@L4T2DYR43N app % pwd
/Users/swathisri.ks/Documents/International_Debt_Analytics_DA2/app


then open the db_connection.py file and make connection.


| Task                   | Where?                  |
| ---------------------- | ----------------------- |
| Load CSV               | `.ipynb`                |
| Data cleaning          | `.ipynb`                |
| Null handling          | `.ipynb` 
| Data transformation    | `.ipynb`                |
| EDA                    | `.ipynb`                |
| MySQL connection       | `.ipynb`                |
| Create database        | `.ipynb`                |
| Create 5 tables        | `.ipynb`                |
| Load 5 CSVs into MySQL | `.ipynb`                |
| Test SQL queries       | `.ipynb`                |
| 30 questions           | `.ipynb`                |
| SQL insights           | `.ipynb`                |
| Streamlit dashboard    | `app.py`                |
| Plotly charts          | `app.py`                |
