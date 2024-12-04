import streamlit as st


def summary_body():

    st.write("### Project Summary")

    st.write("#### 1. Introduction")
    st.write("")
    st.info(
        f"**Loan Default Predictor** **(LDP)** aims to assess institutional\n"
        f"lenders (creditors) represented by a credit analyst to evaluate the\n"
        f"debt applicant default risk.\n"
        f"**LDP** achieves this by exploiting historical Data and machine\n"
        f"learning algorithms to predict potential default cases.\n"
        f"As such, the institutional lender will be able to ensure **85%**\n"
        f"of future credit issuance are risk free.\n"
        f"\nTwo main economic benefits can be achieved by following\n"
        f"loan issuance decisions aided by data and machine learning, these\n"
        f"are:\n"
        f"* 1. Increase the net income by increasing the revenue from\n"
        f"reliable and continuous interest payments.\n"
        f"* 2. Reduce legal proceedings expenses needed to resolve\n"
        f"defaulted cases.\n"
    )

    st.write(
        f"For detailed project description please refer to the\n"
        f"[ReadMe file](https://github.com/ahmedcodein/loan_default)"
    )

    st.write("#### 2. Business Requirements")
    st.write("")

    st.success(
        f"The project has three business requirements:\n"
        f"* 1. The client is interested to have a data analysis study to\n"
        f" understand the general correlations between the variables\n"
        f"in the dataset, so the client can learn the most relevant\n"
        f"variables that can affect\n"
        f"default event.\n"
        f"* 2. The client is interested in creating a classification model\n"
        f"that is able to predict loan applicant default event with high\n"
        f"confidence with precision of at least **85%**.\n"
        f"* 3. The client is interested in identifying typical applicant\n"
        f"profiles and how those profiles relate to a default event.\n"
    )
