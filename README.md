# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the bring your own data project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into your cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked


You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 


## Business Requirements
* Describe your business requirements


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them) 


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

This section is devoted to explain the procedures conducted by the author to deploy and clone SalesWare code. Additionally, for those who are interested to create a fork from the main branch, a dedicated procedure is also provided.

### 1 Heroku

The following procedure is implemented to deploy SalesWare on Heroku platform:

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

### 2. GitHub

The following procedure is followed to create the software repository

1. Go to your repositories 
2. Open CI PP5-template
3. On the top right, click on "Use this template"
4. Click on "Create a new repository"
5. New window opens
6. In the field of "Repository name" type the project name
7. Choose public
8. Then click on "Create repository"

### 3. Clone into Gitpod

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

### 4. Fork

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


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## References 

* [Loan Classification Dataset](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data) is used as the dataset to develop the project.
* [Code Institute study material](https://codeinstitute.net/de/bildungsgutschein/?hsa_acc=8983321581&hsa_cam=16493764737&hsa_grp=1148990625418091&hsa_ad=&hsa_src=o&hsa_tgt=kwd-71812600511432:loc-72&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&msclkid=6245198f3a9b11aeff5f7edfff546ccc&utm_source=bing&utm_medium=cpc&utm_campaign=CI%20-%20DE%20-%20Search%20-%20Brand&utm_term=code%20institute&utm_content=CI%20-%20DE%20-%20Search%20-%20Brand%20-%20Exact).
* Code Institute Walkthrough Projects. The entirety of the code in this project is taken from Code Institute **Churnometer** walkthrough project.
* [scikit-learn documentation](https://scikit-learn.org/dev/index.html).
* [ChatGPT](https://chat.openai.com/auth/login?sso) is used to understand various ML concepts.
* [Google Gemini](https://gemini.google.com/) is used to understand various ML concepts.
* Code Intitute PP5 student project [Airplane Performance Predictor
](https://github.com/GustafEnebog/data-driven-design)

## Acknowledgements

I would like to thank Mr. Mo Shami for his inputs during the project development. I would also like to thank my family for their help and support during the entire time of this course.

