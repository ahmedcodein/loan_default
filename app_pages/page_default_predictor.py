import streamlit as st
import pandas as pd
from src.data_management import loan_default_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_default,
    predict_cluster)


def default_predictor_body():

    # load predict default files
    version = 'v1'
    churn_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_default/{version}/clf_pipeline_feat_eng.pkl')
    churn_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_default/{version}/clf_pipeline_model.pkl")
    default_features = (pd.read_csv(f"outputs/ml_pipeline/predict_default/{version}/X_train.csv")
                        .columns
                        .to_list()
                        )

    # load cluster analysis files
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### Debt Applicant Default Predictor")
    st.info(
        f"* The client is interested in determining whether or not a given\n"
        f"debt applicant will default.\n"
        f"Additionally, the client is interested to know what is\n"
        f" the probability of the outcome. Moreover, the client is\n"
        f"interested in learning from which cluster this debt applicant\n"
        f"does belong to.\n"
    )
    st.write("---")

    # Generate Live Data
    # check_variables_for_UI(default_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        predict_default(
            X_live, default_features, churn_pipe_dc_fe, churn_pipe_model)

        predict_cluster(X_live, cluster_features,
                        cluster_pipe, cluster_profile)


def check_variables_for_UI(default_features, cluster_features):
    import itertools

    # The widgets inputs are the features used in all pipelines
    # We combine them only with unique values
    combined_features = set(
        list(
            itertools.chain(default_features, cluster_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # load dataset
    df = loan_default_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 5 features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5 = st.beta_columns(2)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type
    # (numerical or categorical)
    # and set initial values
    with col1:
        feature = "loan_amnt"
        st_widget = st.number_input(
            label="Requested Loan Amount",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "loan_percent_income"
        st_widget = st.number_input(
            label="Loan to Income Ratio",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "loan_int_rate"
        st_widget = st.number_input(
            label="Applicable Interest Rate",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "person_income"
        st_widget = st.number_input(
            label="Applicant Annual Income",
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "previous_loan_defaults_on_file"
        st_widget = st.selectbox(
            label="Previous Default?",
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    return X_live
