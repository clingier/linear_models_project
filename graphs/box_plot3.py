import plotly.express as px
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv')


x_data = ["Not HER2", "HER2", "HR and ER", "HR not ER", "Not ER", "ER", "Not Bilateral", "Bilateral"]

y_data = [
    df[df.her2 == 0].lrfs,
    df[df.her2 == 1].lrfs,
    df[df.hr_not_er == 0].lrfs,
    df[df.hr_not_er == 1].lrfs,
    df[df.er == 0].lrfs,
    df[df.er == 1].lrfs,
    df[df.pr == 0].lrfs,
    df[df.pr == 1].lrfs,
    df[df.bilateral == 0].lrfs,
    df[df.bilateral == 1].lrfs
]

colors = ['#B1CEE6', '#7BD1C7', '#689FA8', '#1F3451', '#6DB29E', '#B1CEE6', '#7BD1C7', '#689FA8']

fig = go.Figure()

for xd, yd, cls in zip(x_data, y_data, colors):
        fig.add_trace(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls,
            marker={
                'color': '#47535C',
                'size': 2,
                'line': {
                    'color':cls,
                    'width':2
                }
            },
            line_width=1
        )
    )

fig.update_layout(
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=250,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    plot_bgcolor='#F2F8FC',
    showlegend=False
)

fig.show()
fig.write_image("images/box_plot3.pdf")