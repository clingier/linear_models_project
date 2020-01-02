import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import numpy as np
import plotly.graph_objs as go

QUANT_FEATURES = np.array(['age', 'mri_baseline', 'mri_dac', 'mri_interreg', 'mri_presurg', 'rfs', 'rcb'])

df = pd.read_csv('clean_data.csv', index_col=[0])

X = df[[
    "age",
    "her2",
    "bilateral",
    "mri_interreg",
    "rcb",
    "her2_pos",
    "triple_neg",
    "hr_not_er",
    "del_dac"
]]

X = add_constant(X)

res = pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], index=X.columns)

res = res.sort_values(ascending=False)[:8]
values = np.around(res.values, 2)

values = np.hstack((np.array(res.index).reshape(-1, 1), values.reshape(-1, 1))).T
layout = go.Layout(autosize=True, margin={'l': 0, 'r': 0, 't': 20, 'b': 0})
