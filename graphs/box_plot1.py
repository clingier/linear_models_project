import plotly.express as px
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go

df = pd.read_csv('clean_data.csv')
x_data = ["Diameter at baseline", "Diameter after 3 days of chem.", "Diameter at inter-regimen", "Diameter pre-surgery"]
y_data = [df.mri_baseline, df.mri_dac, df.mri_interreg, df.mri_presurg]

colors = ['#B1CEE6', '#7BD1C7', '#689FA8', '#1F3451', '#6DB29E']

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
        dtick=25,
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

fig.write_image("images/box_plot1.pdf")