import streamlit as st

def sidebar():
    st.sidebar.title("⚙️ Controls")
    return st.sidebar.file_uploader("Upload CSV", type=["csv"])