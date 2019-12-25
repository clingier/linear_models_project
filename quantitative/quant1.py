import pandas as pd
import statsmodels.api as sm
import numpy as np
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv', index_col=[0])

df['lrfs'] = np.log(df['rfs'])

y = df['lrfs']

x = df.drop(['lrfs', 'rfs'], axis=1)

results = sm.OLS(y, x).fit()

y = results.resid
x = df['lrfs']


fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x,
        y=y,
        marker=dict(
            color='rgba(71,83,92, 1)'
        ),
        mode='markers'
        )
    )
fig.update_layout(
    plot_bgcolor='#F2F8FC',
    showlegend=False
)

fig.show()