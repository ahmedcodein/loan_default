import streamlit as st


def summary_body():

    st.write("### Project Summary")

    st.write("#### 1. Introduction")
    st.info(
        f"**Loan Default Predictor** **(LDP)** aims to assess institutional lenders\n"
        f"(creditors) represented by a credit analyst to evaluate the debt\n"
        f"applicant default risk.\n"
        f"**LDP** achieves this by exploiting historical Data and machine\n"
        f"learning algorithms to predict potential default cases.\n"
        f"As such, the institutional lender will be able to ensure **85%**\n"
        f"of future credit issuance are risk free.\n"
        f"\nTwo main economic benefits can be achieved by following\n"
        f"loan issuance decisions aided by data, these are:\n"
        f"* 1. Increase the net income by increasing the revenue from\n"
        f"reliable interest continuous payment\n"
        f"* 2. Reduce legal proceedings expenses needed to resolve\n"
        f"defaulted cases.\n"
    )

    st.write(
        f"For detailed project description please refer to the\n"
        f"[ReadMe file](https://github.com/ahmedcodein/loan_default)"
    )

    st.write("#### 2. Business Requirements")

    st.success(
        f"The project has three business requirements:\n"
        f"* 1. The client is interested to have a data analysis study to\n"
        f" understand the general correlations between the variables\n"
        f"in the dataset.\n"
        f"so the client can learn the most relevant variables that can affect\n"
        f"default event.\n"
        f"* 2. The client is interested in creating a classification model\n"
        f"that is able to predict loan applicant default event with high\n"
        f"confidence with high precision of at least **85%**.\n"
        f"* 3. The client is interested in identifying any hidden patterns\n"
        f"in the data to derive conclusions that can benefit the business.\n"
    )
