import pandas as pd
import numpy as np
import statsmodels.api as sm
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv', index_col=[0])
df.drop(['caucasian', 'af_american', 'pac_islander', 'asian'], axis=1, inplace=True)
df.drop('rfs', axis=1, inplace=True)

results = sm.OLS(df['er'], df.drop('er', axis=1)).fit()
df.drop('er', axis=1, inplace=True)

print(results.params)
print(results.pvalues)

values = np.around([results.params, results.pvalues], 3)

values = np.hstack((df.columns.values.reshape(-1, 1), values.T)).T
layout = go.Layout(autosize=True, margin={'l': 0, 'r': 0, 't': 20, 'b': 0})

fig = go.Figure(layout=layout, data=[go.Table(
  header = dict(
    values = ['', 'Estimated Parameteres','P > |t|'],
    line_color='darkslategray',
    fill_color='#1F3451',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values = values,
    line_color='darkslategray',
    fill=dict(color=['#689FA8', 'white']),
    font=dict(color=['white', 'black']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])
# fig.update_layout(
#   title={
#     'text':'Distributions characteristics of the quantitative variables',
#     'y':0.9,
#     'x':0.5,
#     'xanchor': 'center',
#     'yanchor': 'top'
#   },
# )

fig.show()
fig.write_image("images/table3.pdf")