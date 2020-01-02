import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


import plotly.graph_objs as go 
from plotly.subplots import make_subplots


df = pd.read_csv('clean_data.csv', index_col=[0])

X = np.array(df.drop(['lrfs'], axis=1))
y = np.array(df['lrfs'])

# OLS
OLS = LinearRegression()
OLS.fit(X, y)
OLS_prediction = OLS.predict(X)
OLS_resid = (y - OLS_prediction)

# WLS
WLS = LinearRegression()
WLS.fit(X, y, sample_weight= y)
predictions = WLS.predict(X)
WLS_resid = (y - predictions)


### Plot

fig = go.Figure()

# fig = make_subplots(rows=1, cols=2)
# 
# fig.add_trace(
#     go.Scatter(x=OLS_prediction,
#         y=OLS_resid,
#         marker=dict(
#             color='rgba(71,83,92, 1)'
#         ),
#         mode='markers'
#         ),
#     1,
#     1
# )

fig.add_trace(
    go.Scatter(
        y=WLS_resid,
        x=predictions,
        marker=dict(
            color='rgba(71,83,92, 1)'
        ),
        mode='markers'
    ),
)
fig.show()
fig.write_image('images/scatter1.pdf')