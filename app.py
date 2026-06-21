import streamlit as st
import pandas as pd
import sqlite3

# Database Connection
conn = sqlite3.connect("food_wastage.db", check_same_thread=False)

st.set_page_config(page_title="Local Food Wastage Management System", layout="wide")

st.title("🍲 Local Food Wastage Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Home",
     "Dashboard",
     "Food Listings",
     "Provider Contacts"
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

    st.subheader("Claim Status")

    claim_chart = pd.read_sql_query("""
    SELECT Status,
           COUNT(*) AS Total
    FROM claims
    GROUP BY Status
    """, conn)

    st.bar_chart(
        claim_chart.set_index("Status")
    )

# Food Listings
elif menu == "Food Listings":
    st.header("Available Food Listings")

    food = pd.read_sql_query("SELECT * FROM food_listings", conn)

    st.dataframe(food)


elif menu == "Provider Contacts":
    st.header("Provider Contacts")

    contacts = pd.read_sql_query(
        "SELECT Name, City, Contact FROM providers",
        conn
    )

    st.dataframe(contacts)# Paste the complete Streamlit code here
