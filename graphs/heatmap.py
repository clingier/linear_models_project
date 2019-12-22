import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('clean_data.csv', index_col=[0])

c = df.corr()

fig = go.Figure(data=go.Heatmap(
                   z=c,
                   x=df.columns,
                   y=df.columns,
                   hoverongaps = False))
fig.write_image('images/corr.pdf')