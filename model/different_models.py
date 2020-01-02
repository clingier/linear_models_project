import pandas as pd
import statsmodels.api as sm
import numpy as np

df = pd.read_csv('clean_data.csv', index_col=[0])

df['lrfs'] = np.log(df.rfs)

model = sm.OLS(df['lrfs'], df.drop(['lrfs'], axis=1)).fit()

print(model.history)