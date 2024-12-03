import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from src.data_management import loan_default_data, load_pkl_file


def ml_cluster_body():

    # load cluster analysis files and pipeline
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_silhouette = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_silhouette.png")
    features_to_cluster = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/features_define_cluster.png")
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )

    # dataframe for cluster_distribution_per_variable()
    df_loan_status_vs_clusters = loan_default_data().filter(
        ['loan_status'], axis=1)
    df_loan_status_vs_clusters['Clusters'] = cluster_pipe['model'].labels_

    st.write("### ML Pipeline: Cluster Analysis")
    # display pipeline training summary conclusions
    st.info(
        f"* The custer pipeline is fitted with best features\n"
        f"resulted it in a significant improvement in terms of performance\n"
        f"with respect to full features case.\n"
        f"* The pipeline average silhouette score is 0.39."
    )
    st.write("---")

    st.write("#### Cluster ML Pipeline steps")
    st.write(cluster_pipe)

    st.write("#### The features the model was trained with")
    st.write(cluster_features)

    st.write("#### Clusters Silhouette Plot")
    st.image(cluster_silhouette)

    cluster_distribution_per_variable(
        df=df_loan_status_vs_clusters, target='loan_status')

    st.write("#### Most important features to define a cluster")
    st.image(features_to_cluster)

    st.write("#### Cluster Profile")
    statement = (
        f"* Clusters 1 and 2 interpretation shows that default on\n"
        f"previous loan(s) is **100%** risk of default predictor.\n"
        f"In such case, all other features will not be relevant in terms\n"
        f"of predicting a default event.\n"
        f"* Cluster 0 has a typical profile that **must** possess no\n"
        f"defaults on any previous loans with loan-to-income ratio of less\n"
        f"than 11% with a risk of default of **69%**.\n"
        f"* Cluster 3 has typical profile that **must** possess no\n"
        f"default on any previous loans with loan-to-income ratio between\n"
        f"(16% -28%) with a risk of default of **42%**.\n"
        f"* Both 0 and 3 Clusters possess a **counter intuitive**\n"
        f"interpretation.\n"
        f"In there, higher loan-to-income ratio has lower risk of default\n."
        f"Naturally, the opposite should be true, ie. lower loan-to-income\n"
        f"leads to lower risk of default."
        f"The customer should provide additional variables,\n"
        f"for example, the length of loan maturity, pledged collateral,\n"
        f"to assess the truthy of this counter intuitive outcome. Since\n"
        f", the reason that the higher loan-to-income comes with low risk\n"
        f"of default could be attributed to the fact that loan majority\n"
        f"period is so short that it does not make the loan at huge risk."
    )
    st.info(statement)

    statement = (
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


def cluster_distribution_per_variable(df, target):

    df_bar_plot = df.value_counts(["Clusters", target]).reset_index()
    df_bar_plot.columns = ['Clusters', target, 'Count']
    df_bar_plot[target] = df_bar_plot[target].astype('object')

    st.write(f"#### Clusters distribution across {target} levels")
    fig = px.bar(df_bar_plot, x='Clusters', y='Count',
                 color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    # we replaced fig.show() for a streamlit command to render the plot
    st.plotly_chart(fig)

    df_relative = (df
                   .groupby(["Clusters", target])
                   .size()
                   .groupby(level=0)
                   .apply(lambda x:  100*x / x.sum())
                   .reset_index()
                   .sort_values(by=['Clusters'])
                   )
    df_relative.columns = ['Clusters', target, 'Relative Percentage (%)']

    st.write(f"#### Relative Percentage (%) of {target} in each cluster")
    fig = px.line(df_relative, x='Clusters', y='Relative Percentage (%)',
                  color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    fig.update_traces(mode='markers+lines')
    # we replaced fig.show() for a streamlit command to render the plot
    st.plotly_chart(fig)
