import pandas as pd
import numpy as np
from sklearn import linear_model
import numpy as np
import plotly.graph_objs as go
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

df = pd.read_csv('clean_data.csv', index_col=[0])

X = df.drop('lrfs', axis=1)
y = df['lrfs']

model = linear_model.LinearRegression()

sfs1 = sfs(
    model,
    k_features=(1, 17),
    forward=True,
    floating=True,
    verbose=2,
    scoring='r2'
)

sfs1 = sfs1.fit(X, y)

for i in sfs1.k_feature_idx_:
    print(X.columns[i])