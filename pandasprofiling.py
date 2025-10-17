import pandas as pd
from ydata_profiling import ProfileReport

# Load your data
df = pd.read_csv("pakistan_cities_weather.csv")

# Generate profile report
profile = ProfileReport(df, title="Data Report", explorative=True)

# Display in notebook
profile.to_notebook_iframe()

# Or save as HTML file
profile.to_file("data_profile.html")