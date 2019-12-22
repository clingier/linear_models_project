import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import numpy as np

df = pd.read_csv('clean_data.csv', index_col=[0])

X = add_constant(df.drop('rfs', axis=1))

res = pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], index=X.columns)

res = res[res != np.inf]


# values = np.hstack((QUANT_FEATURES.reshape(-1, 1), values.T)).T
# layout = go.Layout(autosize=True, margin={'l': 0, 'r': 0, 't': 20, 'b': 0})


# fig = go.Figure(layout=layout, data=[go.Table(
#   header = dict(
#     values = ['', 'VIF'],
#     line_color='darkslategray',
#     fill_color='#1F3451',
#     align=['left','center'],
#     font=dict(color='white', size=12),
#     height=40
#   ),
#   cells=dict(
#     values = values,
#     line_color='darkslategray',
#     fill=dict(color=['#689FA8', 'white']),
#     font=dict(color=['white', 'black']),
#     align=['left', 'center'],
#     font_size=12,
#     height=30)
#     )
# ])


print(res.sort_values(ascending=False))