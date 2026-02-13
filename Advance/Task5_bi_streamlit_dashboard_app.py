import streamlit as st
import pandas as pd

st.title("Global Superstore Dashboard")

# Load dataset
df = pd.read_csv("superstore.csv")

# Quick look at Dataset
#df.info()
#df.head()
# Dataset don't have any missing or invalid values.

# Sidebar filters

st.sidebar.header("Filters") # Sidebar Title

region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()) # all possible regions
)

category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()) # all possible categories
)

subcategory = st.sidebar.multiselect(
    "Select Sub-Category",
    options=sorted(df["Sub.Category"].unique()) # all possible sub categories
)

# Apply filters
filtered_df = df.copy()

if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]

if category:
    filtered_df = filtered_df[filtered_df["Category"].isin(category)]

if subcategory:
    filtered_df = filtered_df[filtered_df["Sub.Category"].isin(subcategory)]
# show the filterd data
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)

# Key Performance Indicators (KPIs)

st.subheader("Key Performance Indicators")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

# Top 5 customers by sales
top_customers = filtered_df.groupby("Customer.Name")["Sales"].sum().sort_values(ascending=False).head(5)

# Display KPIs in columns
col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

st.subheader("Top 5 Customers by Sales")
st.dataframe(top_customers)

# Add Charts to Dashboard

st.subheader("Sales by Category")
sales_by_category = filtered_df.groupby("Category")["Sales"].sum().reset_index()
st.bar_chart(sales_by_category.set_index("Category"))

st.subheader("Profit by Region")
profit_by_region = filtered_df.groupby("Region")["Profit"].sum().reset_index()
st.bar_chart(profit_by_region.set_index("Region"))

# Conclusion
# The interactive Streamlit dashboard allows users to explore Global Superstore sales 
# and profit data dynamically. With filters for Region, Category, and Sub-Category, 
# it updates key performance indicators (total sales, total profit) and top 5 customers 
# automatically. Visual charts highlight sales by category and profit by region, 
# making it easy to identify trends and business insights. This dashboard provides a 
# simple yet effective tool for business analysis and decision-making.