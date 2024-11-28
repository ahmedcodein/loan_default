from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.summary import summary_body
from app_pages.data_analysis import data_analysis_body
from app_pages.hypotheses import hypothesis_body
from app_pages.predict_default import predict_default_body
from app_pages.cluster import cluster_body

# Create an instance of the app
app = MultiPage(app_name="Loan Default Predictor")

# Add app pages
app.add_page("Project Summary", summary_body)
app.add_page("Data Analysis", data_analysis_body)
app.add_page("Hypotheses", hypothesis_body)
app.add_page("Predict Default", predict_default_body)
app.add_page("Cluster Analysis", cluster_body)

app.run()
