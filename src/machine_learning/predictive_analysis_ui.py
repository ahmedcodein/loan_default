import streamlit as st
import pandas as pd


def predict_default(
    X_live,
    default_features,
    default_pipeline_dc_fe,
    default_pipeline_model
):

    # from live data, subset features related to this pipeline
    X_live_default = X_live.filter(default_features)

    # apply data cleaning / feat engine pipeline to live data
    X_live_default_dc_fe = default_pipeline_dc_fe.transform(X_live_default)

    # predict
    default_prediction = default_pipeline_model.predict(X_live_default_dc_fe)
    default_prediction_proba = default_pipeline_model.predict_proba(
        X_live_default_dc_fe)

    # Create a logic to display the results
    default_prob = default_prediction_proba[0, default_prediction][0]*100
    if default_prediction == 0:
        default_result = 'will'
    else:
        default_result = 'will not'

    statement = (
        f'### There is {default_prob.round(1)}% probability '
        f'that this debt applicant **{default_result} default**.')

    st.write(statement)

    return default_prediction


def predict_cluster(
    X_live, cluster_features,
    cluster_pipeline,
    cluster_profile
):

    # from live data, subset features related to this pipeline
    X_live_cluster = X_live.filter(cluster_features)

    # predict
    cluster_prediction = cluster_pipeline.predict(X_live_cluster)

    statement = (
        f"### The prospect is expected to belong to\n"
        f"**cluster {cluster_prediction[0]}**")
    st.write("---")
    st.write(statement)

    statement = (
        f"* Historically, **debtors in Cluster 0 do tend to default** "
        f"with a probability of 69%.\n"
        f"Whereas in **Cluster 1 and 2, all debtors tend to default**\n"
        f"with a probability of 100% while in **Cluster 3 almost 60% of\n"
        f"debtors do not default**."
    )
    st.info(statement)

    statement = (
        f"The cluster profile interpretation allowed us to label the cluster\n"
        f"in the following fashion:\n"
        f"* Cluster 0: No previous loan default with maximum loan-to-income\n"
        f"11% makes likely (69%) to default.\n"
        f"* Cluster 1: previous loan default lead to 100% default prediction\n"
        f"irrelevant what other features are.\n"
        f"* Cluster 2: previous loan default lead to 100% default prediction\n"
        f"irrelevant what other features are.\n"
        f"* Cluster 3: No previous loan default with maximum loan-to-income\n"
        f"range between (16% -28%) makes unlikely (58%) to default.\n"
    )
    st.success(statement)

    cluster_profile.index = [" "] * len(cluster_profile)
    cluster_profile_df = pd.DataFrame(cluster_profile)
    st.dataframe(cluster_profile_df)
