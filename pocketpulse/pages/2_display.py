import streamlit as st
import pandas as pd 
import plotly.express as px
from database import get_transactions
transactions = get_transactions()
df = pd.DataFrame(transactions,columns=["ID","Purpose","Amount","Category","Date","Type"])
st.title("View all your transactions in one place")
st.dataframe(df)
st.subheader("Credit vs Debit")
total_debit = df[df["Type"] == "Debit"]["Amount"].sum()
total_credit = df[df["Type"]=="Credit"]["Amount"].sum()
summary_df = pd.DataFrame({
    "Transaction Type":["Debit","Credit"],
    "Amount": [total_debit,total_credit]})
bar_chart = px.bar(summary_df, x = "Transaction Type",
                   y = "Amount", color="Transaction Type")
st.plotly_chart(bar_chart)
