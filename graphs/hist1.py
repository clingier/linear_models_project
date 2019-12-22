import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

df = pd.read_csv('clean_data.csv', index_col=[0])

df['rfs_log'] = np.log(df.rfs.values)

trace1 = ff.create_distplot(
    [df.rfs],
    ['Recurrence Free Survival'],
    bin_size=[50],
    histnorm='probability',
    show_rug=False,
    curve_type='normal'
)

trace2 = ff.create_distplot(
    [df.rfs_log],
    ['log(Recurrence Free Survival)'],
    bin_size=[0.05],
    histnorm='probability',
    show_rug=False,
    curve_type='normal'
)

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Histogram(trace1['data'][0], marker_color='#689FA8'), 1, 1)
fig.add_trace(
    go.Scatter(
        trace1['data'][1],
        line=dict(color='#1F3451', width=1)),
    1, 
    1
)


fig.add_trace(
    go.Histogram(
        trace2['data'][0],
        marker_color='#6DB29E'
    ),
    1, 
    2
)

fig.add_trace(
    go.Scatter(
        trace2['data'][1],
        line=dict(color='#1F3451', width=1)
    ),
    1,
    2
)


fig['layout'].update(
    bargap=0.2,
    plot_bgcolor='#F2F8FC'
)

fig.write_image("images/hist1.pdf")