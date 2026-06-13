import streamlit as st
import pandas as pd
import sqlite3

# Database Connection
conn = sqlite3.connect("food_wastage.db", check_same_thread=False)

st.set_page_config(page_title="Local Food Wastage Management System", layout="wide")

st.title("🍲 Local Food Wastage Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Home", "Food Listings", "Provider Contacts"]
)

# Home Page
if menu == "Home":
    st.header("Welcome")
    st.write("""
    This application helps reduce food wastage by connecting food providers with receivers.
    """)

# Food Listings
elif menu == "Food Listings":
    st.header("Available Food Listings")

    food = pd.read_sql_query("SELECT * FROM food_listings", conn)

    st.dataframe(food)

# Provider Contacts
elif menu == "Provider Contacts":
    st.header("Provider Contacts")

    contacts = pd.read_sql_query(
        "SELECT Name, City, Contact FROM providers",
        conn
    )

    st.dataframe(contacts)# Paste the complete Streamlit code here
