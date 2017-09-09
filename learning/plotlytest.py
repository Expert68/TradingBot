import plotly
from plotly.graph_objs import Scatter, Layout, Candlestick
from plotly import figure_factory as FigureFactory


# plotly.offline.plot({
#     "data": [Scatter(x=[0, 1, 2, 3], y=[3, 2, 1, 0]), Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4])],
#     "layout": Layout(title="hello world")
# })



import pandas_datareader.data as web
from datetime import datetime

df = web.DataReader("aapl", 'google', datetime(2007, 10, 1), datetime(2009, 4, 1))
print(df)
fig = FigureFactory.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)

# plotly.offline.plot({
#     "data": [fig],
#     "layout": Layout(title="AAPL")
# })

plotly.offline.plot(fig)
