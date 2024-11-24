from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.summary import summary_body

# Create an instance of the app
app = MultiPage(app_name="Loan Default Predictor")

# Add app pages
app.add_page("Project Summary", summary_body)

app.run()
