import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv', index_col=[0])

X = df[[
    "her2",
    "bilateral",
    "hr_p_her2_neg",
    "hr_not_er",
    "del_dac",
    "rcb_interreg"
]]

X = sm.add_constant(X)

y = df.lrfs

model = sm.WLS(endog=y, exog=X, weights=y)

results = model.fit()

results.summary()

import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(results.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.tight_layout()
plt.savefig('images/SFS_model.png')