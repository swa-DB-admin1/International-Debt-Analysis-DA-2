import streamlit as st
import pandas as pd
import plotly.express as px

from app.db_connection import get_connection


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="International Debt Analytics",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🌍 International Debt Analytics Dashboard")

st.write(
    "Analysis of international debt by country, indicator and year."
)

st.divider()


# -----------------------------
# Database function
# -----------------------------

def run_query(query):

    connection = get_connection()

    df = pd.read_sql(query, connection)

    connection.close()

    return df