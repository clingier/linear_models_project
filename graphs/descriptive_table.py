import plotly.graph_objs as go
import pandas as pd
from scipy.stats import describe
import numpy as np

QUANT_FEATURES = np.array(['age', 'mri_baseline', 'mri_dac', 'mri_interreg', 'mri_presurg', 'rfs', 'rcb'])

QUAL_FEATURES = np.array(['race_id', 'er', 'pr', 'hr', 'her2', 'hr_her_cat', 'bilateral', 'survstat', 'left', 'right', 'rfs_ind'])

df = pd.read_csv('clean_data.csv', index_col=[0])

result = describe(df[QUANT_FEATURES])
std_dev = np.array([np.std(df[column].values) for column in QUANT_FEATURES])

values = np.around([result.mean, std_dev, result.skewness, result.kurtosis], 2)

values = np.hstack((QUANT_FEATURES.reshape(-1, 1), values.T)).T
layout = go.Layout(autosize=True, margin={'l': 0, 'r': 0, 't': 20, 'b': 0})

fig = go.Figure(layout=layout, data=[go.Table(
  header = dict(
    values = ['', 'Mean','Standard Deviation', 'Skewness', 'Kurtosis'],
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
fig.write_image("images/table1.png")