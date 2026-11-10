import streamlit as st
from database import add
st.title("➕ Add your transactions")
with st.form("expense_form", clear_on_submit=True):
    title = st.text_input("Purpose")
    amount = st.number_input("Amount")
    category = st.selectbox("Category",["🍕 Food and drink","📖 Education","✈️ Travel","📺 Entertainment", "🤑 Pocket Money", "😐 Misc"])
    date = st.date_input("Date")
    type = st.radio("Transaction Type", ["Debit","Credit"])
    submit = st.form_submit_button("Add")
    print(f"Title:{title} Amount: {amount} Category: {category} Date: {date} Type: {type}")
    if submit:
        try:
            add(title, amount, category, date,type)
            st.success("Transaction added")
        except Exception as e: st.error(f"Error: {e}")
