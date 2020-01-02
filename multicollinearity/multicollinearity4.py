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
    "er",
    "mri_baseline",
    "mri_interreg",
    "rcb",
    "hr_p_her2_neg",
    "hr_not_er",
    "del_dac",
    "rcb_interreg"
]]

X = add_constant(X)

res = pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], index=X.columns)

res = res.sort_values(ascending=False)[:8]

y = X['rcb_interreg']

X = X.drop('rcb_interreg', axis=1)

sm.OLS(y, X).fit().summary()