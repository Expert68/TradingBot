import time
import backtrader as bt
import backtrader.feeds as btfeeds

import pandas

# Create a cerebro entity
cerebro = bt.Cerebro(stdstats=False)

# Add a strategy
cerebro.addstrategy(bt.Strategy)

# Get a pandas dataframe
datapath = ('../EURUSD_data/DAT_ASCII_EURUSD_M1_2013.csv')


dataframe = pandas.read_csv(datapath,
                            header=None,
                            names = ["Date","Open","High","Low","Close","Volume"],
                            sep=';',
                            parse_dates=True,
                            index_col=0)
dataframe["OpenInterest"] = 0

dataframe = dataframe.resample('5T').agg({'Open': 'first',
                                 'High': 'max',
                                 'Low': 'min',
                                 'Close': 'last',
                                 'Volume':'first',
                                 'OpenInterest':'first'})


print('--------------------------------------------------')
print(dataframe)
print('--------------------------------------------------')

# Pass it to the backtrader datafeed and add it to the cerebro
data = bt.feeds.PandasData(dataname=dataframe)

#cerebro.resampledata(data)
cerebro.adddata(data)

print("resample complete")

start = time.time()

# Run over everything
cerebro.run()

elapsed = (time.time() - start)

print(elapsed)
print("run complete")
# Plot the result
cerebro.plot(style='candle')
