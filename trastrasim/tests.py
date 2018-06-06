from django.test import TestCase

# Create your tests here.
# import talib
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
 
data = ts.get_k_data('399300', index=True, start='2017-01-01', end='2017-06-31')
# sma_10 = talib.SMA(np.array(data['close']), 10)
# sma_30 = talib.SMA(np.array(data['close']), 30)
fig = plt.figure(figsize=(24, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(range(0, len(data['date']), 10))
ax.set_xticklabels(data['date'][::10])
ax.plot(sma_10, label='10 日均线')
ax.plot(sma_30, label='30 日均线')
ax.legend(loc='upper left')
mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                      width=0.5, colorup='r', colordown='green',
                      alpha=0.6)
plt.grid()