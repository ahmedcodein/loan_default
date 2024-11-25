import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import loan_default_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def data_analysis_body():

    # load data
    df = loan_default_data()

    # hard copied from "02 - Data Analysis" notebook
    vars_to_study = [
        'loan_int_rate',
        'loan_percent_income',
        'person_home_ownership',
        'person_income',
        'previous_loan_defaults_on_file',
    ]

    st.write("### Data Analysis")
    st.info(
        f"The client is interested to have a data analysis study to\n"
        f"understand the general correlations between the variables\n"
        f"in the dataset.\n"
    )
    st.write("#### *Data Inspection*")
    # inspect data
    if st.checkbox("Inspect Loan Default Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below is a table that shows the first 10 rows.")

        st.write(df.head(10))

    st.write("---")
    
    st.write("#### *Correlation Study*")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better\n"
        f"understand how the variables are correlated to loan_status levels.\n"
    )
    st.write(
        f"* The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Data Analysis" notebook - "Conclusions" section
    st.info(
        f"From the correlation study the following conclusions are extracted:\n"
        f"1. Pervious loan default has positive and moderate correlation to loan approval.\n"
        f"2. Interest Rate has positive and weak correlation to loan approval.\n"
        f"3. Loan-to-income ratio has positive and weak correlation to loan approval.\n"
        f"4. Home ownership has weak correlation to loan approval.\n"
        f"This correlation exercises two duality depending on home ownership\n"
        f"status (i.e. rent, own and mortgage).\n"
        f"5. Income has negative and very weak correlation to loan approval.\n"
    )

    # Code copied from "02 - Data Analysis" notebook
    df_eda = df.filter(vars_to_study + ['loan_status'])

    # Individual plots per variable
    if st.checkbox("loan_status Levels per Variable"):
        loan_status_level_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in Blue indicates a profile of a defaulted debtor")
        parallel_plot_loan_status(df_eda)


# Code copied from "02 - Data Analysis" notebook,
# "Implementation of EDA on selected variables" section
def loan_status_level_per_variable(df_eda):
    target_var = 'loan_status'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# Code copied from "02 - Data Analysis" notebook,
# "Implementation of EDA on selected variables" section
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var, order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# Code copied from "02 - Data Analysis" notebook,
# "Implementation of EDA on selected variables" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# Code copied from "02 - Data Analysis" notebook,
# Parallel Plot section
def parallel_plot_loan_status(df_eda):

    rate_map = [-np.Inf, 5, 7.5, 10, 12.5, 15, 17.5, 20, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'loan_int_rate': rate_map})
    df_parallel = disc.fit_transform(df_eda)

    n_classes = len(rate_map) - 1
    classes_ranges = disc.binner_dict_['loan_int_rate'][1:-1]
    labels_map = {}
    for n in range(0, n_classes):
        if n == 0:
            labels_map[n] = f"<{classes_ranges[0]}"
        elif n == n_classes-1:
            labels_map[n] = f"+{classes_ranges[-1]}"
        else:
            labels_map[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"

    df_parallel['loan_int_rate'] = df_parallel['loan_int_rate'].replace(
        labels_map)
    fig = px.parallel_categories(
        df_parallel, color="loan_status", color_continuous_scale="bluered")
    fig.update_layout(paper_bgcolor='black')
    st.plotly_chart(fig)
