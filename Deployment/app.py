import streamlit as st
import EDA, predict

st.set_page_config(page_title="Transportation Klasification", layout="wide", initial_sidebar_state="auto")

st.sidebar.title("Navigation")
nav = st.sidebar.selectbox("Go To", ["EDA", "predict"])
if nav == "EDA":
    EDA.run()
else:
    predict.run()
