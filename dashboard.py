import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app.db_connection import get_connection


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="International Debt Analytics",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DARK BLUE DASHBOARD STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #061426;
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #020b18;
        border-right: 1px solid #164e70;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 1600px;
    }

    /* Titles */
    h1, h2, h3 {
        color: white !important;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #0b2942, #082238);
        border: 1px solid #0877a8;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.25);
    }

    div[data-testid="stMetricLabel"] {
        color: #8fc9e8 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #11c5ff !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #10263b;
        color: white;
        border: 1px solid #17688f;
    }

    /* Divider */
    hr {
        border-color: #173c57;
    }

    /* Plotly containers */
    div[data-testid="stPlotlyChart"] {
        background-color: #0a2035;
        border: 1px solid #15577b;
        border-radius: 15px;
        padding: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATABASE
# ============================================================

@st.cache_resource
def get_db_connection():
    return get_connection()


@st.cache_data
def load_data():

    connection = get_db_connection()

    query = """
        SELECT *
        FROM allcountries_debt_data
    """

    df = pd.read_sql(query, connection)

    return df


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = load_data()

except Exception as e:

    st.error("Unable to load data from MySQL.")

    st.exception(e)

    st.stop()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = [
    str(col).strip().lower().replace(" ", "_")
    for col in df.columns
]


# ============================================================
# IDENTIFY IMPORTANT COLUMNS
# ============================================================

def find_column(possible_names):

    for name in possible_names:

        if name in df.columns:
            return name

    return None


country_col = find_column([
    "country_name",
    "country",
    "countryname"
])

indicator_col = find_column([
    "indicator_name",
    "indicator",
    "series_name",
    "series"
])

year_col = find_column([
    "year",
    "year_value"
])

debt_col = find_column([
    "debt",
    "debt_value",
    "amount",
    "value",
    "debt_amount"
])


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Filters")

st.sidebar.write(
    "Use the filters to explore international debt."
)


# Country filter

if country_col:

    countries = sorted(
        df[country_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_country = st.sidebar.selectbox(
        "🌍 Country",
        ["All Countries"] + countries
    )

else:

    selected_country = "All Countries"


# Indicator filter

if indicator_col:

    indicators = sorted(
        df[indicator_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_indicator = st.sidebar.selectbox(
        "📊 Indicator",
        ["All Indicators"] + indicators
    )

else:

    selected_indicator = "All Indicators"


# Year filter

if year_col:

    years = sorted(
        pd.to_numeric(
            df[year_col],
            errors="coerce"
        )
        .dropna()
        .astype(int)
        .unique()
        .tolist()
    )

    selected_year = st.sidebar.selectbox(
        "📅 Year",
        ["All Years"] + years
    )

else:

    selected_year = "All Years"


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df.copy()


if country_col and selected_country != "All Countries":

    filtered_df = filtered_df[
        filtered_df[country_col].astype(str)
        == selected_country
    ]


if indicator_col and selected_indicator != "All Indicators":

    filtered_df = filtered_df[
        filtered_df[indicator_col].astype(str)
        == selected_indicator
    ]


if year_col and selected_year != "All Years":

    filtered_df = filtered_df[
        pd.to_numeric(
            filtered_df[year_col],
            errors="coerce"
        )
        == selected_year
    ]


# ============================================================
# CONVERT DEBT TO NUMERIC
# ============================================================

if debt_col:

    filtered_df[debt_col] = pd.to_numeric(
        filtered_df[debt_col],
        errors="coerce"
    )

    filtered_df = filtered_df.dropna(
        subset=[debt_col]
    )


# ============================================================
# HEADER
# ============================================================

st.title("🌍 International Debt Analytics")

st.caption(
    "Global Debt Distribution  •  Country Analysis  •  "
    "Indicator Analysis  •  Debt Trends"
)

st.divider()


# ============================================================
# TOP METRICS
# ============================================================

total_debt = (
    filtered_df[debt_col].sum()
    if debt_col and not filtered_df.empty
    else 0
)

total_countries = (
    filtered_df[country_col].nunique()
    if country_col
    else 0
)

total_indicators = (
    filtered_df[indicator_col].nunique()
    if indicator_col
    else 0
)

total_years = (
    filtered_df[year_col].nunique()
    if year_col
    else 0
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "💰 TOTAL DEBT",
        f"${total_debt:,.0f}"
    )


with col2:

    st.metric(
        "🌍 COUNTRIES",
        f"{total_countries:,}"
    )


with col3:

    st.metric(
        "📊 INDICATORS",
        f"{total_indicators:,}"
    )


with col4:

    st.metric(
        "📅 YEARS",
        f"{total_years:,}"
    )


st.divider()


# ============================================================
# COUNTRY-WISE DEBT DISTRIBUTION
# ============================================================

st.header("🏆 Country-wise Debt Distribution")


if country_col and debt_col and not filtered_df.empty:

    country_debt = (
        filtered_df
        .groupby(country_col)[debt_col]
        .sum()
        .reset_index()
        .sort_values(
            debt_col,
            ascending=False
        )
    )

    top_10 = country_debt.head(10)

    bottom_10 = (
        country_debt
        .sort_values(debt_col)
        .head(10)
    )


    left, right = st.columns(2)


    # --------------------------------------------------------
    # TOP COUNTRIES
    # --------------------------------------------------------

    with left:

        st.subheader("🔝 Top 10 Countries with Highest Debt")

        fig_top = px.bar(
            top_10.sort_values(debt_col),
            x=debt_col,
            y=country_col,
            orientation="h",
            color=debt_col,
            color_continuous_scale="Blues"
        )

        fig_top.update_layout(
            template="plotly_dark",
            height=450,
            showlegend=False,
            coloraxis_showscale=False,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        st.plotly_chart(
            fig_top,
            use_container_width=True
        )


    # --------------------------------------------------------
    # LOWEST COUNTRIES
    # --------------------------------------------------------

    with right:

        st.subheader("🔻 10 Countries with Lowest Debt")

        fig_bottom = px.bar(
            bottom_10.sort_values(debt_col),
            x=debt_col,
            y=country_col,
            orientation="h",
            color=debt_col,
            color_continuous_scale="Teal"
        )

        fig_bottom.update_layout(
            template="plotly_dark",
            height=450,
            showlegend=False,
            coloraxis_showscale=False,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        st.plotly_chart(
            fig_bottom,
            use_container_width=True
        )


# ============================================================
# DEBT DISTRIBUTION + INDICATORS
# ============================================================

st.header("📊 Debt Distribution Across Indicators")


if indicator_col and debt_col and not filtered_df.empty:

    indicator_debt = (
        filtered_df
        .groupby(indicator_col)[debt_col]
        .sum()
        .reset_index()
        .sort_values(
            debt_col,
            ascending=False
        )
    )

    top_indicators = indicator_debt.head(10)


    left, right = st.columns(2)


    # --------------------------------------------------------
    # INDICATOR BAR CHART
    # --------------------------------------------------------

    with left:

        st.subheader("📊 Top Debt Indicators")

        fig_indicator = px.bar(
            top_indicators.sort_values(debt_col),
            x=debt_col,
            y=indicator_col,
            orientation="h",
            color=debt_col,
            color_continuous_scale="Viridis"
        )

        fig_indicator.update_layout(
            template="plotly_dark",
            height=500,
            showlegend=False,
            coloraxis_showscale=False,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        st.plotly_chart(
            fig_indicator,
            use_container_width=True
        )


    # --------------------------------------------------------
    # DONUT CHART
    # --------------------------------------------------------

    with right:

        st.subheader("🌐 Debt Share by Indicator")

        pie_data = indicator_debt.head(8)

        fig_pie = px.pie(
            pie_data,
            values=debt_col,
            names=indicator_col,
            hole=0.55,
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig_pie.update_layout(
            template="plotly_dark",
            height=500,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )


# ============================================================
# DEBT TRENDS
# ============================================================

st.header("📈 International Debt Trends")


if year_col and debt_col and not filtered_df.empty:

    trend = (
        filtered_df
        .groupby(year_col)[debt_col]
        .sum()
        .reset_index()
    )

    trend[year_col] = pd.to_numeric(
        trend[year_col],
        errors="coerce"
    )

    trend = trend.sort_values(year_col)


    left, right = st.columns(2)


    # --------------------------------------------------------
    # LINE GRAPH
    # --------------------------------------------------------

    with left:

        st.subheader("📈 Debt Trend Over Time")

        fig_trend = px.line(
            trend,
            x=year_col,
            y=debt_col,
            markers=True
        )

        fig_trend.update_traces(
            line=dict(
                width=4,
                color="#00C8FF"
            ),
            marker=dict(
                size=8
            )
        )

        fig_trend.update_layout(
            template="plotly_dark",
            height=450,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis_title="Year",
            yaxis_title="Total Debt"
        )

        st.plotly_chart(
            fig_trend,
            use_container_width=True
        )


    # --------------------------------------------------------
    # AREA GRAPH
    # --------------------------------------------------------

    with right:

        st.subheader("📊 Debt Growth Pattern")

        fig_area = px.area(
            trend,
            x=year_col,
            y=debt_col
        )

        fig_area.update_traces(
            line_color="#00E5A8",
            fillcolor="rgba(0,229,168,0.25)"
        )

        fig_area.update_layout(
            template="plotly_dark",
            height=450,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            xaxis_title="Year",
            yaxis_title="Debt"
        )

        st.plotly_chart(
            fig_area,
            use_container_width=True
        )


# ============================================================
# COUNTRY COMPARISON
# ============================================================

st.header("🌎 Country Debt Comparison")


if country_col and debt_col and not filtered_df.empty:

    comparison = (
        filtered_df
        .groupby(country_col)[debt_col]
        .sum()
        .reset_index()
        .sort_values(
            debt_col,
            ascending=False
        )
        .head(15)
    )


    fig_compare = px.bar(
        comparison,
        x=country_col,
        y=debt_col,
        color=country_col,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig_compare.update_layout(
        template="plotly_dark",
        height=500,
        showlegend=False,
        xaxis_tickangle=-45,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )


# ============================================================
# DATA TABLE
# ============================================================

with st.expander("📋 View Underlying Debt Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌍 International Debt Analytics | "
    "Data-driven decision making through country, "
    "indicator and trend analysis"
)