import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def ml_default_body():

    version = 'v1'
    # load needed files
    default_pipe_dc_fe = load_pkl_file(
        f"outputs/ml_pipeline/predict_default/{version}/"
        f"clf_pipeline_feat_eng.pkl")
    default_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_default/{version}/"
        f"clf_pipeline_model.pkl")
    default_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_default/{version}/"
        f"features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_default/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_default/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_default/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_default/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Default")
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming at least 0.85 precision on\n"
        f"'Default (0)' class, since we are interested in this project in "
        f" detecting a potential debtor Default.\n"
        f"* The pipeline performance on train and test set is **1** and \n"
        f"**0.95**, respectively."
    )

    # show pipelines
    st.write("---")
    st.write("### 1. Pipelines")
    st.write("")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(
        f"* The first is responsible for feature engineering.\n"
        f"> **Note**: No **cleaning** is included since the original dataset\n"
        f"comes\n"
        f"already cleaned"
    )
    st.write("##### 1.1. Feature Engineering Pipeline")
    st.write(default_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write("##### 1.2. Feature Scaling and Modelling Pipeline")
    st.write(default_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write(
        "* The features the model was trained on ranked based on their"
        " importance.")
    st.write(X_train.columns.to_list())
    st.image(default_feat_importance)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### 2. Pipeline Performance")
    st.write("")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=default_pipe_model,
                    label_map=["Default", "No Default"])
