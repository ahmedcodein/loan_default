from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.page_summary import summary_body
from app_pages.page_data_analysis import data_analysis_body
from app_pages.page_hypotheses import hypothesis_body
from app_pages.page_ml_default import ml_default_body
from app_pages.page_cluster import ml_cluster_body
from app_pages.page_default_predictor import default_predictor_body

# Create an instance of the app
app = MultiPage(app_name="Loan Default Predictor")

# Add app pages
app.add_page("Project Summary", summary_body)
app.add_page("Data Analysis", data_analysis_body)
app.add_page("Hypotheses", hypothesis_body)
app.add_page("ML: Predict Default", ml_default_body)
app.add_page("ML: Cluster Analysis", ml_cluster_body)
app.add_page("Default Predictor", default_predictor_body)

app.run()
