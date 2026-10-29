import streamlit as st

st.title("AI Tools App")

name = st.text_input("Enter your name")

if name:
    st.success("Good Morning, " + name + "! 😊 \n How are you?  🙂 ")
