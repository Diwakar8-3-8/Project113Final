import pandas as pd
import statistics
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()