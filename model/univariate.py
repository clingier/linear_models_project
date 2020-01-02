import pandas as pd

import numpy as np

import statsmodels.api as sm

import plotly.graph_objs as go


df = pd.read_csv('clean_data.csv', index_col=[0])

y = df.lrfs

df.drop('lrfs', axis=1, inplace=True)

columns = df.columns

coefs = []
pvalues = []
conf_intervals = []

for i in range(df.shape[1]):
    X = df.iloc[:,i]
    X = sm.add_constant(X)

    model = sm.WLS(y, X, weights=y)
    results = model.fit()

    coefs.append(results.params[columns[i]])
    pvalues.append(results.pvalues[columns[i]])
    conf_intervals.append(results.conf_int().loc[columns[i], :])

pvalues = pd.Series(pvalues, index=columns)
coefs = pd.Series(coefs, index=columns)
conf_intervals = pd.DataFrame(conf_intervals)

n_df = pd.concat([conf_intervals, pvalues, coefs], axis=1)

n_df.set_axis(["Conf_0", "Conf_1", "pvalues", "coefs"], axis='columns')

n_df.pvalues = n_df.pvalues.apply(lambda x: str(np.around(x, 4)))
n_df.Conf_0 = n_df.Conf_0.apply(lambda x: str(np.around(x, 4)))
n_df.Conf_1 = n_df.Conf_1.apply(lambda x: str(np.around(x, 4)))
n_df.coefs = n_df.coefs.apply(lambda x: str(np.around(x, 4)))

n_df['coefs_int'] = n_df.apply(lambda row: f"{row['coefs']} ({row['Conf_0']};{row['Conf_1']})", axis=1)

n_df = n_df[["coefs_int", "pvalues"]]

n_df = n_df.reset_index()

values = n_df.values

fig = go.Figure(data=[go.Table(
  header = dict(
    values = ['', 'Coefficients (95% Conf. Interval)', 'P > |t|'],
    line_color='darkslategray',
    fill_color='#1F3451',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values = values.T,
    line_color='darkslategray',
    fill=dict(color=['#689FA8', 'white']),
    font=dict(color=['white', 'black']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])

fig.update_layout(
    autosize=False,
    height=800,
)

fig.write_image('images/univariate.pdf')