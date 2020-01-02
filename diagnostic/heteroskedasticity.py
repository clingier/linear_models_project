import pandas as pd
import statsmodels.stats.diagnostic
import statsmodels.api as sm
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv('clean_data.csv')

y = df['lrfs']

X = df[[
    "age",
    "er",
    "mri_baseline",
    "mri_interreg",
    "rcb",
    "hr_p_her2_neg",
    "hr_not_er",
    "del_dac",
    "rcb_interreg"
]]

X['mri_baseline'] = X['mri_baseline'] ** 3
# X['mri_interreg'] = X['mri_interreg'] ** 3
# X['rcb_interreg'] = X['rcb_interreg'] ** 3

X = sm.add_constant(X)

model = sm.OLS(y, X)

results = model.fit()

white_test = sm.stats.diagnostic.het_white(results.resid, results.model.exog)
labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']


white_test = np.around(white_test, 3).reshape(-1, 1)
labels = np.array(labels).reshape(-1, 1)

values = np.hstack([labels, white_test])

fig = go.Figure(data=[go.Table(
  header = dict(
    values = ['', 'Value'],
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
    height=400,
)

# fig.write_image('images/hetero.pdf')
fig.show()