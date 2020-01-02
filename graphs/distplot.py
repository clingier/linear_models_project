import pandas as pd
import plotly.graph_objects as go
import numpy as np



df = pd.read_csv('clean_data.csv', index_col=[0])


x = df.rcb_baseline
y = df.lrfs

fig = go.Figure()
fig.add_trace(go.Histogram2dContour(
        x = x,
        y = y,
        colorscale = 'Blues',
        reversescale = True,
        xaxis = 'x',
        yaxis = 'y'
    ))
fig.add_trace(go.Histogram(
        y = y,
        xaxis = 'x2',
        nbinsx=50,
        marker = dict(
            color = '#1F3451'
        )
    ))
fig.add_trace(go.Histogram(
        x = x,
        yaxis = 'y2',
        nbinsx=50,
        marker = dict(
            color = '#1F3451'
        )
    ))

fig.update_layout(
    autosize = False,
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    xaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    yaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    height = 800,
    width = 800,
    bargap = 0,
    hovermode = 'closest',
    showlegend = False
)

fig.show()

fig.write_image('images/2d_box_plot.pdf')
