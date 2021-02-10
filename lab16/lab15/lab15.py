import math

import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


def countFirstEquation(x):
    return (x ** 0.5) * math.sin(10 * x)


def countSecondEquation(x):
    return 5 * math.sin(10 * x) * math.sin(3 * x)


if __name__ == '__main__':
    x_array = []
    y_array = []
    for i in np.arange(0, 5.5, 0.5):
        x_array.append(i)
        y_array.append(countFirstEquation(i))
    plt.plot(x_array, y_array)
    plt.ylabel('y')
    plt.xlabel('X')
    plt.title('First Equation')
    plt.legend(['Y(x)=x^(1/2)*sin(10*x), x=[0...5]'])
    plt.savefig('first.png')
    plt.close()
    x_array = []
    y_array = []
    for i in np.arange(0, 4.5, 0.5):
        x_array.append(i)
        y_array.append(countFirstEquation(i))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_array, y=y_array, name="Y(x)=5*sin(10*x)*sin(3*x), x=[0...4]"))
    fig.add_trace(go.Scatter(x=[0], y=[0], name="0"))
    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      title="Second Equation",
                      xaxis_title="X Axis",
                      yaxis_title="Y Axis",
                      margin=dict(l=0, r=0, t=30, b=0))
    fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
    fig.update_layout()
    fig.write_html("second.html")
    fig.show()
