import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Database Connection
conn = sqlite3.connect("food_wastage.db", check_same_thread=False)

st.set_page_config(page_title="Local Food Wastage Management System", layout="wide")

st.title("🍲 Local Food Wastage Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["🏡Home",
     "📈Dashboard",
     "🍱Food Listings",
     "📡Provider Contacts"
    ]
)

# Home Page
if menu == "Home":
    st.header("Welcome")
    st.write("""
    This application helps reduce food wastage by connecting food providers with receivers.
    """)

# Dashboard
elif menu == "Dashboard":

    st.header("📊 Dashboard")

    total_providers = pd.read_sql_query(
        "SELECT COUNT(*) AS cnt FROM providers", conn
    ).iloc[0,0]

    total_receivers = pd.read_sql_query(
        "SELECT COUNT(*) AS cnt FROM receivers", conn
    ).iloc[0,0]

    total_food = pd.read_sql_query(
        "SELECT COUNT(*) AS cnt FROM food_listings", conn
    ).iloc[0,0]

    total_claims = pd.read_sql_query(
        "SELECT COUNT(*) AS cnt FROM claims", conn
    ).iloc[0,0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Providers", total_providers)
    col2.metric("Receivers", total_receivers)
    col3.metric("Food Listings", total_food)
    col4.metric("Claims", total_claims)

    st.subheader("🥧 Claims by Status")

claim_status = pd.read_sql_query("""
SELECT Status,
       COUNT(*) AS Total
FROM claims
GROUP BY Status
""", conn)

fig = px.pie(
        claim_status,
        names="Status",
        values="Total",
        title="Claims by Status",
        
        color_discrete_sequence=px.colors.qulitative.Set3
    )
st.plotly_chart(fig,
    use_container_width=True)

st.subheader("📊 Food Available by Type")

food_type = pd.read_sql_query("""
SELECT Food_Type,
       COUNT(*) AS Total
FROM food_listings
GROUP BY Food_Type
""", conn)

fig = px.bar(
        food_type,
        x="Food_Type",
        y="Total",
        title="Food Available by Type",
        color_discrete_sequence=px.colors.qulitative.Bold
    )
st.plotly_chart(fig,
    use_container_width=True)

st.subheader("🏢 Listings by Provider Type")

provider_type = pd.read_sql_query("""
SELECT Provider_Type,
       COUNT(*) AS Total
FROM food_listings
GROUP BY Provider_Type
""", conn)

fig = px.bar(
        provider_type,
        x="Provider_Type",
        y="Total",
        title="Listings by Provider Type",
        color_discrete_sequence=px.colors.qulitative.Set2
    )
st.plotly_chart(fig,
    use_container_width=True)

st.subheader("🍽️ Claims by Meal Type")

meal_type = pd.read_sql_query("""
SELECT Meal_Type,
       COUNT(*) AS Total
FROM food_listings
GROUP BY Meal_Type
""", conn)

fig = px.pie(
        meal_type,
        names="Meal_Type",
        values="Total",
        title="Claims by Meal Type",
        color_discrete_sequence=px.colors.qulitative.Pastel
    )
st.plotly_chart(fig,
    use_container_width=True)
