# Introduction

**Loan Default Predictor (LDP)** aims to assess institutional lenders (creditors) represented by a credit analyst to evaluate the debt applicant default risk. LDP achieves this by exploiting historical Data and machine learning algorithms to predict potential default cases. As such, the institutional lender will be able to ensure 85% of future credit issuance are risk free.

Two main economic benefits can be achieved by following loan issuance decisions aided by data and machine learning, these are:

1. Increase the net income by increasing the revenue from reliable and continuous interest payments.
2. Reduce legal proceedings expenses needed to resolve defaulted cases.

The live link to the project is provided in [Loan Default Predictor](https://loan-default-ml-predictor-a4d2d7adf5ae.herokuapp.com/)

![Central Bank](images/introduction.jpg)

# Dataset

The dataset is imported from [kaggle](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data). The dataset contains 14 attributes. Each attribute describes a specific trait of a pervious debtor. In the dataset, these attributes are represented by columns. While each row, describes a debtor, who either defaulted or not.

The dataset consists of 14 attributes (variables). From these, 9 are numeric and 5 are text (categorical - object). The dataset contains 45000 records. A summary of the dataset is provided in the table below:

| Variable                       | Description                                               | Data Type   |
| ------------------------------ | --------------------------------------------------------- | ----------- |
| person_age                     | Age of the person                                         | Float       |
| person_gender                  | Gender of the person                                      | Categorical |
| person_education               | Highest education level                                   | Categorical |
| person_income                  | Annual income                                             | Float       |
| person_emp_exp                 | Years of employment experience                            | Integer     |
| person_home_ownership          | Home ownership status (e.g., rent, own, mortgage)         | Categorical |
| loan_amnt                      | Loan amount requested                                     | Float       |
| loan_intent                    | Purpose of the loan                                       | Categorical |
| loan_int_rate                  | Loan interest rate                                        | Float       |
| loan_percent_income            | Loan amount as a percentage of annual income              | Float       |
| cb_person_cred_hist_length     | Length of credit history in years                         | Float       |
| credit_score                   | Credit score of the person                                | Integer     |
| previous_loan_defaults_on_file | Indicator of previous loan defaults                       | Categorical |
| loan_status (target variable)  | Loan approval status: **Default = 0**, **No Default = 1** | Integer     |


# Business Requirements

The project has three business requirements:

1. The client is interested to have a data analysis study to understand the general correlations between the variables in the dataset, so the client can learn the most relevant variables that can affect default event.
2. The client is interested in creating a classification model that is able to predict loan applicant default event with high confidence with precision of at least 85%.
3. The client is interested in identifying typical applicant profiles and how those profiles relate to a default event.


# Project Hypotheses

Upon embarking on this project, four hypotheses are considered. The first and the fourth hypotheses are validated, while the second and the third hypotheses proved to be invalid. The author suspects that the second and the third hypotheses are not validated because the original kaggel dataset did not include them. Those variables are essential in holding some critical information, if available could potentially change the model and subsequently the validity of the aforementioned hypotheses. For example, from the author perspective, those variable might be the length of the loan, other source of incomes (passive income) or other outstanding loans.

The four hypotheses are listed here with their respective validation discussions:

1. **Default on previous loan(s) makes it unlikely to guarantee a free risk loan (free of default)**.   
   - **How to Validate**:There are two possibility for validating the hypothesis. First by conducting a parallel plot wheres the author would be able to see how default on pervious loan affects the loan_status outcome. Second by conducting a cluster analysis and evaluate if some clusters with pervious defaults clearly lead to defaults.
   - **Evaluation Result**: *The hypothesis is validated in both the parallel plot and in the cluster analysis conducted in notebook 02 and 05-b respectively*.
2. **The higher the loan-to-income ratio, the higher the probability of loan default**.
   - **How to Validate**: The suggested approach is by conducting a cluster analysis and evaluate if some clusters with higher loan-to-income ratio lead to defaults.
   - **Evaluation Result**:*In notebook 05-b, Cluster Analysis, cluster profiles reveal that the opposite is true. That is the higher the loan-to-income ratio the lower the risk of default. From the author perspective, this is attributed to the absence of critical variables in the original dataset that could explain this counterintuitive result, such as Loan Length,other source of incomes (passive income) or other outstanding loans*.
3. **However high a person's income, it does not impact no default if the loan-to-income ratio is below a defined threshold**.
   - **How to Validate**: The suggested approach is by conducting a cluster analysis and evaluate if some clusters with change in expected loan_status would be impacted by the ratio of loan-to-income ratio.
   - **Evaluation Result**: *This hypothesis appears to be invalid, for the same reason in the presented in hypothesis 2*.
4. **If a debtor rents their home and has no record of default, the likelihood of no default is guaranteed**.
   - **How to Validate**: The suggested approach is by conducting a parallel plot wheres the author would be able to see if the two conditions met, ie home ownership is equivalent to rent and has no record of default will guarantee default free risk.
   - **Evaluation Result**: *The parallel plot analysis in notebook 02 reveals that the initial hypothesis is not entirely accurate but holds some truth in it. While renters tend to have a lower default rate compared to debtors with other home ownership types, it does not guarantee a risk-free loan*.

# Business Mapping

In this section, the business requirements are mapped to the data visualization and ML tasks based on the following rational:

1. **Business Requirement 1**: Correlation study and data visualization
   - We will inspect the data related to the loan default debtor
   - We will conduct a correlation study using Pearson and Spearman method along with Predictive Power Score. This is to understand how variables are correlated to loan_status which is the target variable. 
   - We will plot the most relevant variables from the correlation study against the loan_status.
   - We will plot the parallel plot against the loan_status to interactively visualize the relationship between the correlated variables and the loan_status.
2. **Business Requirement 2**: Data Analysis and Classification Model
   - We want to predict if a debt applicant will default or not. Hence, we want to build a binary classifier.
3. **Business Requirement 3**: Data Analysis and Cluster Model
   - We want to cluster similar debtors to predict to which cluster a new debt applicant belongs to. 
   - We want to predict what is the probability of that specific debt applicant to default or not based on the cluster the applicant belongs to.

# ML Business Case

## 1. Classification Model

We want to predict if a debt applicant will default or not. Hence, we want to build a binary classifier. The target variable used for the prediction is loan_default. Whereas
default = 0 and no default = 1.
Hence, the following logic is considered:
- we consider a classification model for the job. It is based on supervised learning with two classes and single label.
- The model goal is: 
  - predict loan default applicant with a precision of at least 85%.
- The model will be considered a failure if the default precision is less than 85%.
- The Dataset used to train and test the model is imported from Kaggle. Please refer to the [Dataset section](#dataset) for further information. 

## 1. Cluster Model

We want to cluster similar debtor to predict to which cluster a new debt applicant belongs to. We want to predict what is the probability of that specific debt applicant to default or not based on the cluster the applicant belongs to.
Hence, the following logic is considered:
- The model success metrics:
  - Silhouette score is at least 2
  - The number of clusters should not be higher than 6 clusters
- we consider a KMeans clustering model (unsupervised learning) for the job.
- We consider standard clustering pipeline with principle component analysis.
- We consider both all the features in the dataset as well as the important features to assess which pipeline shall serve the goal best.
- The Dataset used to train and test the model is imported from Kaggle. Please refer to the [Dataset section](#dataset) for further information. 

# Epics and User Stories

Agile methodology is used to develop Loan Default Predictor. The high-level requirements presented in the previous section are followed to define the six Epics of the project. Those Epics are then broke down into 36 User Stories. The Epics and the user stories along with how development conducted over each sprint can be accessed on [Jira-Loan Default Prediction Project](https://almudhafar4codeinstitute.atlassian.net/jira/software/projects/LDP/boards/6/timeline)

**Epic LDP-1 Data Collection**\
*Description:* This Epic is concerned with collecting, downloading and saving the dataset.

  - **User Story: Dataset Download**
    - As a data practitioner, I can collect the dataset from Kaggel to the workspace so I can download the dataset and unzip it.
  - **User Story: Data Saving**
    - As a data practitioner, I can save the collected dataset from Kaggel in a directory in the workspace so I can use the data for the analysis stage.
  
**Epic LDP-2 Data Analysis**\
*Description:* This Epic is concerned with analyzing the dataset.

  - **User Story: Data Loading**
    - As a data practitioner, I can load the dataset from workspace so I can begin the data analysis step.
  - **User Story: Data Profiling**
    - As a data practitioner, I can profile the dataset so I can understand the dataset variables and asses if any transformation is needed or there are any missing data.
  - **User Story: Correlation Analysis**
    - As a data practitioner, I can apply different correlation methods so I can understand the relationship between the variables and the target.
  - **User Story: Important Feature Distributions**
    - As a data practitioner, I can evaluate the distribution of the most relevant variables along the target to get better feeling about those features.
  - **User Story: Variables Parallel Plot**
    - As a data practitioner, I can visualize the parallel plot of all the important features against the target variable so I can have a better feeling about their relationships with the target variable.

**Epic LDP-3 Data Cleaning and Feature Engineering**\
*Description:* This Epic is concerned with cleaning and feature engineer the dataset based on the Data analysis epic outcome.

  - **User Story: Data Cleaning**
    - As a data practitioner, I can clean the dataset so I can further preprocess the data for feature engineering step.
  - **User Story: Feature Engineering**
    - As a data practitioner, I can feature engineer the dataset so I can prepare the data to the split the dataset into train and test datasets.
  - **User Story: Data Split**
    - As a Data Practitioner, I can split the data into a train and test datasets so I can prepare the datasets for for the next steps.
    
**Epic LDP-4 Loan Default Prediction**\
*Description:* This Epic is concerned with developing the best ML model that is able to predict a default event.

  - **User Story: Data Split**
    - As a Data Practitioner, I can split the data into a train and test datasets so i can prepare the datasets for the Data Cleaning and Feature Engineering Pipeline.
  - **User Story: Data Cleaning and Feature Engineering**
    - As a Data Practitionar, I want to create a Data Cleaning and Feature Engineering so that I can prepare the data for the ML Pipeline. 
  - **User Story: Best Algorithm and Hyperparameter Configuration**
    - As a Data Practitioner, I can search for the best ML algorithm and its Hyperparameter so I can create an ML pipeline.
  - **User Story: ML Model Performance**
    - As a ML Engineer, I can evaluate the ML model performance so I can suffice the business requirement of predicting a default on loan.
  - **User Story: Delete Opportunity Entry**
    - As a Site User, I can delete the opportunity so that I can remove it from the database.
  - **User Story: Best Features**
    - As a data practitioner, I can identify the best features so I can build an new ML pipeline with the same configuration to compare its performance with the ML pipeline with the full features.

**Epic LDP-5 Cluster Analysis**\
*Description:* This Epic is concerned with developing a Cluster pipeline to extract hidden profiles withing the data.

  - **User Story: Data Loading**
    - As a data practitioner, I can load the dataset into the Cluster Analysis notebook so I can prepare the dataset for the analysis.
  - **User Story: Define Cluster Pipeline with all features**
    - As a data practitioner, I can define a cluster pipeline so I can apply it to the full features dataset.
  - **User Story: Apply Cluster Pipeline on all features**
    - As a data practitioner, I can apply cluster pipeline to the full features dataset so I can evaluate the cluster pipeline performance.
  - **User Story: Dataset Split with all features dataset**
    - As a data practitioner, I can split the dataset into Train and Test Sets and apply the cluster pipeline I can evaluate the cluster pipeline performance.
  - **User Story: Number of Clusters with all features**
    - As a data practitioner, I can use Elbow method and Silhouette score to extract the optimum number of clusters..
  - **User Story: Cluster Performance with all features**
    - As a data practitioner, I can evaluate the performance of the cluster pipeline prediction to evaluate if the cluster is able to predict with good confidence.
  - **User Story: Important Features**
    - As a data practitioner, I can read the cluster profiles so I can extract and analyze cluster profiles patterns.
  - **User Story: Cluster Profile with all features** 
    - As a data practitioner, I can read the cluster profiles so I can extract and analyze cluster profiles patterns.
  - **User Story: Define Cluster Pipeline with best features** 
    - As a data practitioner, I can define a cluster pipeline so I can apply it to the full features dataset.
  - **User Story: Apply Cluster Pipeline with best features** 
    - As a data practitioner, I can apply cluster pipeline to the full features dataset so I can evaluate the cluster pipeline performance.
  - **User Story: Number of Clusters with best features** 
    - As a data practitioner, I can use Elbow method and Silhouette score to extract the optimum number of clusters.
  - **User Story: Dataset Split with best features dataset** 
    - As a data practitioner, I can split the dataset into Train and Test Sets and apply the cluster pipeline I can evaluate the cluster pipeline performance.
  - **User Story: Cluster Performance with best features** 
    - As a data practitioner, I can evaluate the performance of the cluster pipeline prediction to evaluate if the cluster is able to predict with good confidence.
  - **User Story: Cluster Profile with best features** 
    - As a data practitioner, I can read the cluster profiles so I can extract and analyze cluster profiles patterns.
  - **User Story: Push output to the repo** 
    - As a data practitioner, I can save all the output files from the cluster analysis with best features in the repo so I can use them from the dashboard.

**Epic LDP-6 Dashboard Development and Deployment**\
*Description:* This Epic is concerned with developing and deploying a dashboard aiming to present the outcome of the project in a user friendly manner.

  - **User Story: Project Summary**
    - As a credit analyst, I can view a page that contains the project summary so that I can understand what the project is about, what the business requirements are and how to navigate the tool dashboards.
  - **User Story: Data Analysis**
    - As a credit practitioner, I can view a page that contains the statistical analysis conducted on the datasets by the data practitioner so I can see how the data are analyzed and visualized. 
  - **User Story: Project Hypotheses**
    - As a credit analyst, I can view a page that contains the project hypotheses and how the data practitioner approached the validations and whether each hypothesis is validated or not.
  - **User Story: ML: Predict Default**
    - As a credit analyst, I can view Predictor Model Evaluation report so I can understand the predictor model performance.
  - **User Story: ML: Cluster Analysis**
    - As a credit analyst I can view a page that contains Debtor Default Profiles so I can understand typical patterns of Debtor Default Profile.
  - **User Story: Default Predictor**
    - As a credit analyst I can enter a set of features into the ML model so that I can see the probability of the debtor applicant being defaulted and to which cluster the debtor applicant belongs to.

# Dashboard Design

## 1. Project Summary
The following aspects are to be viewed in the project summary page:
  - Introduction: A summary of the project intend and main goal with a description of main business benefit expected from the project
  - Business Requirements: a list of the business requirements
## 2. Data Analysis
The following aspects are to be viewed in the data analysis page:
  - Page Aim: A description of the main intend of this page.
  - Dataset Listing: Providing an access to the dataset to allow the user to view the dataset.
  - Correlation Study: Enable the user to view the correlated variables and summary of how those correlated to target variable. It also shows the target variable level to each of extracted variables. Finally, the ability to view the parallel plot. 
## 3. Hypotheses
The following aspects are to be viewed in the Hypotheses page:
  - Discussion: a brief discussion on the main findings following the hypotheses validation.
  - Hypotheses: listing the hypotheses with an explanation how each of the hypotheses is evaluated
## 4. ML: Predict Default
The following aspects are to be viewed in the ML Predict Default page:
  - Introduction: a brief discussion on the main goal of the ML pipeline.
  - Pipelines: Definitions of the developed pipelines with the ability to display them.
  - Features: Displaying the features the pipelines are trained on.
  - Pipeline Performance: Displaying two reports on the ML pipeline performance on the train and test datasets respectively.
## 5. ML: Cluster Analysis
The following aspects are to be viewed in the ML: Cluster Analysis page:
  - Introduction: a brief discussion on pipeline main result.
  - Pipeline: Definitions of the developed pipeline with the ability to display the pipeline steps.
  - Features: Displaying the features the pipelines are trained on.
  - Plots: Displaying Silhouette, cluster distribution over the target variable, relative percentage of target variable to each cluster and a plot to display best features to define a cluster
  - Cluster Profile Summary: displaying a description of each cluster profile with a discussion on each cluster. Additionally, displaying a table that shows cluster profiles.
## 6. Default Predictor
The following aspects are to be viewed in the ML: Cluster Analysis page:
  - Introduction: description the main goal of the predictor.
  - Predictor Interface: Listing the important features as inputs for the user with a button of running the prediction.
  - Result: Showing the prediction result with description of the results meaning.

# Manual Tests

This subsection provides a comprehensive account of the manual tests conducted for this project. The tests follows the epics structure. The test and their respective acceptance criteria along with test results are presented below:

**Epic LDP-1 Data Collection**\
*Description:* This Epic is concerned with collecting, downloading and saving the dataset.

  - **User Story: Dataset Download**
    - As a data practitioner, I can collect the dataset from Kaggel to the workspace so I can download the dataset and unzip it.
      - Acceptance Criterion:
        - Given the dataset is located in the Kaggel website, the data practitioner can download the dataset and then unzip the dataset -- **Pass**
  - **User Story: Data Saving**
    - As a data practitioner, I can save the collected dataset from Kaggel in a directory in the workspace so I can use the data for the analysis stage.
      - Acceptance Criterion:
        - Given the dataset is unzipped, the data practitioner can save the dataset on the workspace -- **Pass**
  
**Epic LDP-2 Data Analysis**\
*Description:* This Epic is concerned with analyzing the dataset.

  - **User Story: Data Loading**
    - As a data practitioner, I can load the dataset from workspace so I can begin the data analysis step.
      - Acceptance Criterion:
        - Given the dataset is saved in the workspace, the data practitioner can load the dataset into the data analysis notebook -- **Pass**
  - **User Story: Data Profiling**
    - As a data practitioner, I can profile the dataset so I can understand the dataset variables and asses if any transformation is needed or there are any missing data.
      - Acceptance Criterion:
        - Given the dataset is loaded into the data analysis notebook, the data practitioner can profile every dataset variable to asses if nay transformation is needed or there are any missing data -- **Pass**
  - **User Story: Correlation Analysis**
    - As a data practitioner, I can apply different correlation methods so I can understand the relationship between the variables and the target.
      - Acceptance Criterion:
        - Given the dataset is loaded into the data analysis notebook, the data practitioner can perform correlation study to understand the relationship between the variables and the target variable -- **Pass**
  - **User Story: Important Feature Distributions**
    - As a data practitioner, I can evaluate the distribution of the most relevant variables along the target to get better feeling about those features.
      - Acceptance Criterion:
        - Given that the most correlated features are extracted from the correlation study, the data practitioner can perform distribution analysis of each correlated feature against the target variable  -- **Pass**
  - **User Story: Variables Parallel Plot**
    - As a data practitioner, I can visualize the parallel plot of all the important features against the target variable so I can have a better feeling about their relationships with the target variable.
      - Acceptance Criterion:
        - Given that the most correlated features are extracted from the correlation study, the data practitioner implement the parallel plot on the features against the target variable -- **Pass**

**Epic LDP-3 Data Cleaning and Feature Engineering**\
*Description:* This Epic is concerned with cleaning and feature engineer the dataset based on the Data analysis epic outcome.

  - **User Story: Data Cleaning**
    - As a data practitioner, I can clean the dataset so I can further preprocess the data for feature engineering step.
      - Acceptance Criterion:
        - Given the dataset loaded into the data cleaning and features engineering notebook, the data practitioner can asses the data for any cleaning processing task and clean the dataset accordingly -- **Pass**
  - **User Story: Feature Engineering**
    - As a data practitioner, I can feature engineer the dataset so I can prepare the data to the split the dataset into train and test datasets.
      - Acceptance Criterion:
        - Given that the dataset is cleaned via data cleaning process step, the data practitioner can perform the feature engineering process on the dataset -- **Pass**
  - **User Story: Data Split**
    - As a Data Practitioner, I can split the data into a train and test datasets so I can prepare the datasets for for the next steps.
      - Acceptance Criterion:
        - Given that the dataset is cleaned and feature engineered via the data cleaning and feature engineering steps, the data practitioner can split the dataset into train and test datasets -- **Pass**
    
**Epic LDP-4 Loan Default Prediction**\
*Description:* This Epic is concerned with developing the best ML model that is able to predict a default event.

  - **User Story: Data Split**
    - As a Data Practitioner, I can split the data into a train and test datasets so i can prepare the datasets for the Data Cleaning and Feature Engineering Pipeline.
      - Acceptance Criterion:
        - Given that the dataset is loaded into the predict default notebook, the data practitioner can split the dataset into train and test datasets -- **Pass**
  - **User Story: Data Cleaning and Feature Engineering**
    - As a Data Practitioner, I want to create a Data Cleaning and Feature Engineering so that I can prepare the data for the ML Pipeline.
      - Acceptance Criterion:
        - Given that the the data cleaning and feature engineering steps are clarified from the data cleaning and feature engineering notebook, the data practitioner can create a data cleaning and feature engineering pipeline -- **Pass** 
  - **User Story: Best Algorithm and Hyperparameter Configuration**
    - As a Data Practitioner, I can search for the best ML algorithm and its Hyperparameter so I can create an ML pipeline.
      - Acceptance Criterion:
        - Given that the dataset is cleaned and feature engineered via the respective pipeline, the ML Engineer can feed the dataset into various ML algorithms to create an ML Pipeline -- **Pass**
  - **User Story: ML Model Performance**
    - As a ML Engineer, I can evaluate the ML model performance so I can suffice the business requirement of predicting a default on loan.
      - Acceptance Criterion:
        - Given that the best ML model is identified, the ML engineer can evaluate the performance of the selected model -- **Pass**
  - **User Story: Best Features**
    - As an ML Engineer, I can identify the best features so I can build an new ML pipeline with the same configuration to compare its performance with the ML pipeline with the full features.
      - Acceptance Criterion:
        - Given that the best ML model is identified, the ML engineer can identify the best features on the identified model and build new ML pipeline based on the best features instead of all the features -- **Pass**

**Epic LDP-5 Cluster Analysis**\
*Description:* This Epic is concerned with developing a Cluster pipeline to extract hidden profiles withing the data.

  - **User Story: Data Loading**
    - As a data practitioner, I can load the dataset into the Cluster Analysis notebook so I can prepare the dataset for the analysis.
      - Acceptance Criterion:
        - Given the dataset is saved in the workspace, the data practitioner can load the dataset into the cluster analysis notebook -- **Pass**
  - **User Story: Define Cluster Pipeline with all features**
    - As a data practitioner, I can define a cluster pipeline so I can apply it to the full features dataset.
      - Acceptance Criterion:
        - Given the dataset is loaded into the notebook, the data practitioner can define a cluster pipeline with all features -- **Pass**
  - **User Story: Dataset Split with all features dataset**
    - As a data practitioner, I can split the dataset into Train and Test Sets and apply the cluster pipeline I can evaluate the cluster pipeline performance.
      - Acceptance Criterion:
        - Given the dataset is loaded into the notebook, the data practitioner can split the dataset into train and test sets -- **Pass**
  - **User Story: Apply Cluster Pipeline on all features**
    - As a data practitioner, I can apply cluster pipeline to the full features dataset so I can evaluate the cluster pipeline performance.
      - Acceptance Criterion:
        - Given cluster pipeline is defined and the dataset with all features is split into train and test, the data practitioner can apply a cluster pipeline on train set -- **Pass**
  - **User Story: Number of Clusters with all features**
    - As a data practitioner, I can use Elbow method and Silhouette score to extract the optimum number of clusters.
      - Acceptance Criterion:
        - Given cluster pipeline is defined and the dataset with all features is split into train and test, the data practitioner can apply Elbow method and Silhouette score to extract the optimum number of clusters -- **Pass**
  - **User Story: Cluster Performance with all features**
    - As a data practitioner, I can evaluate the performance of the cluster pipeline prediction to evaluate if the cluster is able to predict with good confidence.
      - Acceptance Criterion:
        - Given cluster pipeline is applied, the data practitioner can perform performance analysis on the defined cluster pipeline -- **Pass**
  - **User Story: Cluster Profile with all features** 
    - As a data practitioner, I can read the cluster profiles so I can extract and analyze cluster profiles patterns.
      - Acceptance Criterion:
        - Given cluster pipeline is applied, the data practitioner can extract and analyze patterns from the cluster profiles -- **Pass**
  - **User Story: Important Features**
    - As a data practitioner, I can extract the best features so I can build a dataset of best features to be used for the Cluster Profile patterns analysis.
      - Acceptance Criterion:
        - Given cluster pipeline is applied, the data practitioner can extract the best features -- **Pass**
  - **User Story: Define Cluster Pipeline with best features** 
    - As a data practitioner, I can define a cluster pipeline so I can apply it to the full features dataset.
      - Acceptance Criterion:
        - Given best features are identified, the data practitioner can define a cluster pipeline on the best features -- **Pass**
  - **User Story: Apply Cluster Pipeline with best features** 
    - As a data practitioner, I can apply cluster pipeline to the full features dataset so I can evaluate the cluster pipeline performance.
      - Acceptance Criterion:
        - Given the cluster pipeline with best features are defined, the data practitioner can apply the cluster pipeline on the best features -- **Pass**
  - **User Story: Number of Clusters with best features** 
    - As a data practitioner, I can use Elbow method and Silhouette score to extract the optimum number of clusters.
      - Acceptance Criterion:
        - Given cluster pipeline is defined with best features, the data practitioner can apply Elbow method and Silhouette score to extract the optimum number of clusters -- **Pass**
  - **User Story: Dataset Split with best features dataset** 
    - As a data practitioner, I can split the dataset into Train and Test Sets and apply the cluster pipeline I can evaluate the cluster pipeline performance.
      - Acceptance Criterion:
        - Given best features identified, the data practitioner can split the dataset with the selected features only into train and test sets -- **Pass**
  - **User Story: Cluster Performance with best features** 
    - As a data practitioner, I can evaluate the performance of the cluster pipeline prediction to evaluate if the cluster is able to predict with good confidence.
      - Acceptance Criterion:
        - Given cluster pipeline is applied on the best features, the data practitioner can perform performance analysis on the defined cluster pipeline -- **Pass**
  - **User Story: Cluster Profile with best features** 
    - As a data practitioner, I can read the cluster profiles so I can extract and analyze cluster profiles patterns.
      - Acceptance Criterion:
        - Given cluster pipeline is applied on the best features, the data practitioner can extract and analyze patterns from the cluster profiles -- **Pass**
  - **User Story: Push output to the repo** 
    - As a data practitioner, I can save all the output files from the cluster analysis with best features in the repo so I can use them from the dashboard.
      - Acceptance Criterion:
        - Given cluster pipeline performance is accepted, the data practitioner can save the relevant outputs needed for the streamlit dashboard -- **Pass**

**Epic LDP-6 Dashboard Development and Deployment**\
*Description:* This Epic is concerned with developing and deploying a dashboard aiming to present the outcome of the project in a user friendly manner.

  - **User Story: Project Summary**
    - As a credit analyst, I can view a page that contains the project summary so that I can understand what the project is about, what the business requirements are and how to navigate the tool dashboards.
      - Acceptance Criterion:
        - Given credit analyst clicked on the app website link, the credit analyst can land on the project summary page and finds on this page the project introduction and the business requirements of the project -- **Pass**
  - **User Story: Data Analysis**
    - As a credit practitioner, I can view a page that contains the statistical analysis conducted on the datasets by the data practitioner so I can see how the data are analyzed and visualized.
      - Acceptance Criterion:
        - Given credit analyst is on any page of the project, the credit analyst can click on the Data Analysis page to inspect the datasets, gets a summary on the correlation study with all its relevant graphs -- **Pass**
  - **User Story: Project Hypotheses**
    - As a credit analyst, I can view a page that contains the project hypotheses and how the data practitioner approached the validations and whether each hypothesis is validated or not.
      - Acceptance Criterion:
        - Given that the credit analyst is on any page of the project, the credit analyst can click on the Hypotheses page in order to read the project hypotheses and how those hypotheses are validated -- **Pass**
  - **User Story: ML: Predict Default**
    - As a credit analyst, I can view Predictor Model Evaluation report so I can understand the predictor model performance.
      - Acceptance Criterion:
        - Given that the credit analyst is on any page of the project, the credit analyst can click on the ML: Predict Default page in order to read all the pipeline steps and view the ML pipeline performance -- **Pass**
  - **User Story: ML: Cluster Analysis**
    - As a credit analyst I can view a page that contains Debtor Default Profiles so I can understand typical patterns of Debtor Default Profile.
      - Acceptance Criterion:
        - Given that the credit analyst is on any page of the project, the credit analyst can click on the ML: Cluster Analysis page in order to read all the pipeline steps, Silhouette Plot, Cluster distributions, graph of important features and a table on cluster distribution with description -- **Pass**
  - **User Story: Default Predictor**
    - As a credit analyst I can enter a set of features into the ML model so that I can see the probability of the debtor applicant being defaulted and to which cluster the debtor applicant belongs to.
      - Acceptance Criterion:
        - Given that the credit analyst is on any page of the project, the credit analyst can click on theDefault Predictor page and can enter the live data into the prediction model and get the prediction report -- **Pass**

# Python Code Validation

All python codes in the app_pages, src and the app.py folders are validated with CI Python Linter. The code are clean free of errors or warnings.

# Unfixed Bugs

There are no bugs encountered during the development or during the deployment phase.

# Deployment

This section is devoted to explain the procedures conducted by the author to deploy and clone Loan Default Predictor code. Additionally, for those who are interested to create a fork from the main branch, a dedicated procedure is also provided.

## 1. Heroku

The following procedure is implemented to deploy Loan Default Predictor on Heroku platform:

1. Sign in to Heroku account on Heroku dashboard, click on "Create a new app" button
2. Within the "Create New App" window, go to the "App name" input field and type in an App name
3. Within the same window, choose your region from the "Choose region" dropdown menu
4. Click on "Create app" button
5. New window opens for the App that is just created
6. Now go to the "Deploy" tap right at the top of the window
7. Within the "Deployment method" row, click on "GitHub" button
8. Within the "Connect to GitHub" (One row down the Deployment method) click on "Connect to GitHub"
9. Wait a bit for loading
10. Now on the same row and within the search field, type the name of the project repository and click on "Search" button
11. Now click connect
12. Once it is connected to the project repository, scroll down to "Manual Deploy"
13. Within this row, click on "Deploy Branch"
14. Once the deploy log is finished, a message appears and hopefully says: "You app was successfully deployed"
15. Below it a "View" button appears as well
16. Click on the "View" to open the deployed project on a new browser tap 

**Note: Throughout the development, the author chooses only the manual deployment.**

## 2. GitHub

The following procedure is followed to create the software repository

1. Go to your repositories 
2. Open CI PP5-template
3. On the top right, click on "Use this template"
4. Click on "Create a new repository"
5. New window opens
6. In the field of "Repository name" type the project name
7. Choose public
8. Then click on "Create repository"

## 3. Clone into Gitpod

The following procedure is implemented to clone from the GiTHub repo into Gitpod:

1. Go to the "code" in the upper right corner
2. Select "local" 
3. Select "Clone/HTTPs"
4. Copy the url provided
5. Open new browser tap
6. Open your Gitpod Workspace
7. Click on "Create new workspace"
8. Click on "select new Repository"
9. Paste the url in input window
10. Click continue

## 4. Fork

For any person interested to work on the source code of this project, here is the procedure that needs to be followed to make a fork.

1. Go to ahmedcodein repositories
2. Click on "loan_default" repo
3. In the upper right corner, click of "fork" drop down menu
4. Click on "create new fork"
5. Create new fork window opens
6. Select the "owner" of the repo
7. Add a name to "Repository name"
8. Add a description to the "Description" field if needed
9. Click on "Create fork"


# Technologies Used

In this section a list of the technologies used to develop this project is provided below:

| Technology       | Description                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Python           | Programming Language                                                                                               |
| GitHub           | Development Platform                                                                                               |
| Gitpod           | Cloud Development Environment                                                                                      |
| streamlit        | Open-source framework for foe data scientists and AI/ML engineers enables them to deliver interactive applications |
| Heroku           | Development Platform                                                                                               |
| CI Python Linter | Code Institute Python code style convention checker                                                                |

# Main Python Modules and Libraries

In this section a list the libraries used to develop the project with a description as to what purpose each package is used for.

| Technology          | Description                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| os                  | Python module to interacting with the operating system                                                                               |
| pandas              | Python library for data analysis and manipulation                                                                                    |
| numpy               | Python library for large and multi-dimensional arrays and matrices computation                                                       |
| ydata_profiling     | Python library for generating reports on dataset for exploratory data analysis and data quality assessment Platform                  |
| ppscore             | Python package is used as a metric to ass the predictive power of one variable on another                                            |
| feature_engine      | Python library for feature engineering, providing a variety of transformers to handel missing values, encoding, etc.                 |
| matplotlib.pyplot   | Python library for static and interactive visualizations                                                                             |
| scikit-learn        | Python library for machine learning                                                                                                  |
| xgboost             | Open Source for regularizing gradient boosting framework                                                                             |
| SciPy               | Python library for scientific computing and engineering tasks                                                                        |
| joblib              | Python library used to simplify and optimize tasks related ot data processing and machine learning pipelines                         |
| yellowbrick.cluster | Part of yellowbrick library for visualizing and evaluating clustering algorithms and assess the performance of the clustering models |
| warnings            | Python warning control                                                                                                               |


# References 

* [Loan Classification Dataset](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data) is used as the dataset to develop the project.
* [Code Institute study material](https://codeinstitute.net/de/bildungsgutschein/?hsa_acc=8983321581&hsa_cam=16493764737&hsa_grp=1148990625418091&hsa_ad=&hsa_src=o&hsa_tgt=kwd-71812600511432:loc-72&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&msclkid=6245198f3a9b11aeff5f7edfff546ccc&utm_source=bing&utm_medium=cpc&utm_campaign=CI%20-%20DE%20-%20Search%20-%20Brand&utm_term=code%20institute&utm_content=CI%20-%20DE%20-%20Search%20-%20Brand%20-%20Exact).
* Code Institute Walkthrough Projects. The entirety of the code in this project is taken from Code Institute **Churnometer** walkthrough project.
* [scikit-learn documentation](https://scikit-learn.org/dev/index.html).
* [ChatGPT](https://chat.openai.com/auth/login?sso) is used to understand various ML concepts.
* [Google Gemini](https://gemini.google.com/) is used to understand various ML concepts.
* Code Intitute PP5 student project [Airplane Performance Predictor
](https://github.com/GustafEnebog/data-driven-design)
* [Leonardo](https://app.leonardo.ai/) is used to create the introduction image of the README file.

# Acknowledgements

I would like to thank Mr. Mo Shami for his inputs during the project development. I would also like to thank my family for their help and support during the entire time of this course.

