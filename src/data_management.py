import streamlit as st
import pandas as pd
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def loan_default_data():
    df = pd.read_csv("outputs/datasets/collection/row/LoanDefaultDataset.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
