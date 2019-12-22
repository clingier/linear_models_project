import numpy as np
import pandas as pd
import statsmodels.api as sm
import random
import plotly.express as px
import plotly.graph_objs as go

random.seed(42)

df = pd.read_csv('clean_data.csv', index_col=[0])

df = df[['age', 'er', 'pr', 'hr', 'hr_her_cat', 'mri_baseline', 'mri_dac', 'mri_interreg', 'mri_presurg', 'rfs']]

pop = set([i for i in range(10)])

choices = []
parameters_array = []
ith_parameters = []
parameters = []

for i in range(10):

    # get a new independent variable index
    choice = random.sample(pop, k=1)

    #store it in the choosen ones
    choices.append(choice[0])

    #remove it from the population
    pop.remove(choice[0])

    #select the variables
    df_i = df.iloc[:, choices]

    # model with the choosen variables
    model = sm.OLS(df['rfs'], df_i).fit()

    #save the number of parameters and the value of the estimated params
    parameters_array.append(model.params)

    for j in range(i):
        ith_parameters.append(i)
        parameters.append(model.params[j])

stds = []
means = []

for params in parameters_array:
    stds.append(np.std(params))
    means.append(np.mean(params))

y = means
y_upper = [i+s for i,s in zip(means, stds)]
y_lower = [i-s for i,s in zip(means, stds)]

x = [i for i in range(10)]
x_rev = x[::-1]

trace1 = go.Scatter(
    x = x + x_rev,
    y = y_upper + y_lower,
    fill='tozerox',
    fillcolor='rgba(104,159,168,0.3)',
    line = dict(color='rgba(255, 255, 255, 0)'),
    showlegend=False,
)

trace2 = go.Scatter(
    x= x,
    y=y,
    mode='lines',
    line=dict(color='rgba(31,52,81, 0.5)')
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=ith_parameters,
        y=parameters,
        marker=dict(
            color='rgba(71,83,92, 1)'
        ),
        mode='markers'
        )
    )
fig.add_trace(trace1)
fig.add_trace(trace2)
fig.update_layout(
    plot_bgcolor='#F2F8FC',
    showlegend=False
)


fig.write_image('images/m_collinearity.pdf')