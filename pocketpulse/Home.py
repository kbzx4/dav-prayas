import streamlit as st

lcol,rcol= st.columns(2,vertical_alignment="center")
with lcol:
    st.title("PocketPulse - Let your money make sense")
    st.button("Get started")
with rcol:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToFSZIh9V4GDoEnvnRYk0f7U6LNycDR2kfUD_8KvLICw&s=10")

#st.set_page_config(layout="wide",page_title="Pocket Pulse",page_icon="🥀")
#st.title("Hello,World")
#st.subheader("Welcome to Prayas 2.0")
#st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ441sQsWjRUVqRH4kQETJHLVwb2ndVpFGSDyn_Dd5FhA&s=10")
