import streamlit as st


def hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.write("#### 1. Discussions")

    st.info(
        f"Upon embarking on this project, **four hypotheses are considered**\n"
        f". The first three hypotheses are validated by conducting a cluster\n"
        f"analysis, please refer to **Notebook 05-a, conclusion section**.\n\n"
        f"**The fourth hypotheses**, however, could not be validated except\n"
        f"by analyzing the parallel plot of **Data Analysis Notebook 02**.\n"
        f"It should be noted that such validation is subjective.Therefore,\n"
        f"further investigation is necessary to validate the truthy\n"
        f"of the fourth hypothesis.\n"
    )

    st.write("#### 2. Hypotheses")

    st.success(
        f"* 1. Default on previous loan(s) makes it unlikely to acquire new \n"
        f"loan.\n"
        f"* 2. The higher the loan_percent_income, the higher the\n"
        f"probability of rejecting the loan\n"
        f"* 3. However high a person's income, it does not impact loan\n"
        f"approval if the loan_to_income ratio is below a defined threshold.\n"
        f"* 4. If debtor has rented home and has no record of default,\n"
        f"the likelihood of approving loan is guaranteed.\n"
    )
