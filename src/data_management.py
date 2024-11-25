import streamlit as st
import pandas as pd


@st.cache_data()
def loan_default_data():
    df = pd.read_csv("outputs/datasets/collection/row/LoanDefaultDataset.csv")
    return df
