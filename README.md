# Introduction

**Loan Default Predictor (LDP)** aims to assess institutional lenders (creditors) represented by a credit analyst to evaluate the debt applicant default risk. LDP achieves this by exploiting historical Data and machine learning algorithms to predict potential default cases. As such, the institutional lender will be able to ensure 85% of future credit issuance are risk free.

Two main economic benefits can be achieved by following loan issuance decisions aided by data and machine learning, these are:

1. Increase the net income by increasing the revenue from reliable and continuous interest payments.
2. Reduce legal proceedings expenses needed to resolve defaulted cases.

The live link to the project is provided in [Loan Default Predictor](https://loan-default-ml-predictor-a4d2d7adf5ae.herokuapp.com/)

# Business Requirements

The project has three business requirements:

1. The client is interested to have a data analysis study to understand the general correlations between the variables in the dataset, so the client can learn the most relevant variables that can affect default event.
2. The client is interested in creating a classification model that is able to predict loan applicant default event with high confidence with precision of at least 85%.
3. The client is interested in identifying typical applicant profiles and how those profiles relate to a default event.


# Project Hypotheses

Upon embarking on this project, four hypotheses are considered . The first and the fourth hypotheses are validated, while the second and the third hypotheses proved to be invalid The author suspects that the second and the third hypotheses are not validated due to some missing variables in the original dataset that are essential for training the model, for example, the length of the loan, other incomes or other outstanding loans.

The four hypotheses are listed here with their respective validation discussions:

1. Default on previous loan(s) makes it unlikely to acquire new loan. The hypothesis is validated in both the parallel plot and in cluster analysis conducted in notebook 02 and 05-b respectively.
2. The higher the loan-to-income ratio, the higher the probability of rejecting the loan. In notebook 05-b, Cluster Analysis, cluster profiles reveal that the opposite is true. That is the higher loan-to-income ratio the lower the risk of default. From the author perspective, this is attributed to the lack of data variables in the dataset that could explain this counterintuitive result, such as Loan Length.
3. However high a person's income, it does not impact loan approval if the loan-to-income ratio is below a defined threshold. This hypothesis appears to be invalid, for the same reason in the presented in hypothesis 2.
4. If a debtor rents their home and has no record of default, the likelihood of no defaulting on loan is guaranteed. The parallel plot analysis in notebook 02 reveals that the initial hypothesis is not entirely accurate. While renters tend to have a lower default rate compared to debtors with other home ownership types, it does not guarantee a risk-free loan.

# The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


# ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


# Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



# Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

# Deployment

This section is devoted to explain the procedures conducted by the author to deploy and clone Loan Default Predictor code. Additionally, for those who are interested to create a fork from the main branch, a dedicated procedure is also provided.

## 1 Heroku

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


# Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


# References 

* [Loan Classification Dataset](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data) is used as the dataset to develop the project.
* [Code Institute study material](https://codeinstitute.net/de/bildungsgutschein/?hsa_acc=8983321581&hsa_cam=16493764737&hsa_grp=1148990625418091&hsa_ad=&hsa_src=o&hsa_tgt=kwd-71812600511432:loc-72&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&msclkid=6245198f3a9b11aeff5f7edfff546ccc&utm_source=bing&utm_medium=cpc&utm_campaign=CI%20-%20DE%20-%20Search%20-%20Brand&utm_term=code%20institute&utm_content=CI%20-%20DE%20-%20Search%20-%20Brand%20-%20Exact).
* Code Institute Walkthrough Projects. The entirety of the code in this project is taken from Code Institute **Churnometer** walkthrough project.
* [scikit-learn documentation](https://scikit-learn.org/dev/index.html).
* [ChatGPT](https://chat.openai.com/auth/login?sso) is used to understand various ML concepts.
* [Google Gemini](https://gemini.google.com/) is used to understand various ML concepts.
* Code Intitute PP5 student project [Airplane Performance Predictor
](https://github.com/GustafEnebog/data-driven-design)

# Acknowledgements

I would like to thank Mr. Mo Shami for his inputs during the project development. I would also like to thank my family for their help and support during the entire time of this course.

