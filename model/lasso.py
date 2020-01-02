import pandas as pd
import statsmodels.api as sm
import numpy as np
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv', index_col=[0])

y = df.lrfs
X = df.drop('lrfs', axis=1)
X = sm.add_constant(X)

model = sm.WLS(y, X, weights=y)

results = model.fit_regularized(alpha=0.01)

print(results.params)

values = results.params.reset_index().values

fig = go.Figure(data=[go.Table(
  header = dict(
    values = ['', 'Coefs'],
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

fig.write_image('images/lasso_coefs.pdf')

zeroed = results.params.reset_index()
zeroed = zeroed[zeroed[0] == 0]['index']

results = sm.WLS(y, X.drop(zeroed, axis=1), weights=y).fit()

print(results.summary())

import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(results.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.tight_layout()
plt.savefig('images/LASSO_model.png')