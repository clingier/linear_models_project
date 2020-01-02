import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import numpy as np
import plotly.graph_objs as go

QUANT_FEATURES = np.array(['age', 'mri_baseline', 'mri_dac', 'mri_interreg', 'mri_presurg', 'rfs', 'rcb'])

df = pd.read_csv('clean_data.csv', index_col=[0])

X = add_constant(df.drop('rfs', axis=1))

res = pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], index=X.columns)

res = res[res != np.inf]
res = res.sort_values(ascending=False)[:8]
values = np.around(res.values, 2)

values = np.hstack((np.array(res.index).reshape(-1, 1), values.reshape(-1, 1))).T
layout = go.Layout(autosize=True, margin={'l': 0, 'r': 0, 't': 20, 'b': 0})


fig = go.Figure(layout=layout, data=[go.Table(
  header = dict(
    values = ['', 'VIF'],
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
    font=dict(color=['#F7FAFA', 'black']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])

fig.write_image('images/table4.pdf')