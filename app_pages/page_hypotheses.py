import streamlit as st


def hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.write("#### 1. Discussions")
    st.write("")

    st.info(
        f"Upon embarking on this project, **four hypotheses are considered**\n"
        f". The first and the fourth hypotheses are validated,\n"
        f"while the second and the third hypotheses proved to be invalid\n"
        f"The author suspects that the second and the third hypotheses are\n"
        f"not validated due to some missing variables in the original\n"
        f"dataset that are essential for training the model, for example,\n"
        f"the length of the loan, other incomes or other outstanding loans.\n"
    )

    st.write("#### 2. Hypotheses")
    st.write("")

    st.success(
        f"1. **Default on previous loan(s) makes it unlikely to acquire new \n"
        f"loan**.\n"
        f"The hypothesis is validated in both the parallel plot and in\n"
        f"cluster analysis conducted in notebook 02 and 05-b respectively.\n"
        f"2. **The higher the loan-to-income ratio, the higher the\n"
        f"probability of rejecting the loan**.\n"
        f"In notebook 05-b, Cluster Analysis, cluster profiles reveal\n"
        f"that the opposite is true. That is the higher loan-to-income ratio\n"
        f"the lower the risk of default.\n"
        f"From the author perspective, this is attributed to the lack of\n"
        f"data variables in the dataset that could explain this\n"
        f"counterintuitive result, such as Loan Length.\n"
        f"3. **However high a person's income, it does not impact loan\n"
        f"approval if the loan-to-income ratio is below a defined\n"
        f"threshold**.\n"
        f"This hypothesis appears to be invalid, for the same reason in the\n"
        f"presented in hypothesis **2**.\n"
        f"4. **If a debtor rents their home and has no record of default,\n"
        f"the likelihood of no defaulting on loan is guaranteed.**\n"
        f"The parallel plot analysis in notebook 02 reveals that the initial\n"
        f"hypothesis is **not entirely accurate**. While renters tend\n"
        f"to have a lower default rate compared to debtors with other home\n"
        f"ownership types, it does not guarantee a risk-free loan."
    )
