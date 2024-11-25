import streamlit as st
import pandas as pd


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def loan_default_data():
    df = pd.read_csv("outputs/datasets/collection/row/LoanDefaultDataset.csv")
    return df
