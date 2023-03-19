from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
from utility.linear_regression import *
from utility.curve_fitting import *
from utility.graph_analysis import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

yf.pdr_override()


symbol = input("Please input a correct stock symbol: ")
df = pdr.get_data_yahoo(symbol, datetime.today()-relativedelta(months=8), datetime.today())
series = df['Close']
series.index = np.arange(series.shape[0])

month_diff = series.shape[0] // 30
if month_diff == 0:
    month_diff = 1

smooth = int(2 * month_diff + 3)

pts = savitzky_golay_filter(series, smooth, 3)

relative_min, relative_max = relative_min_max(pts)

relative_min_slope, relative_min_int = linear_regression(relative_min)
relative_max_slope, relative_max_int = linear_regression(relative_max)
support = (relative_min_slope * np.array(series.index)) + relative_min_int
resistance = (relative_max_slope * np.array(series.index)) + relative_max_int
current = (0 * np.array(series.index)) + series.values[-1]

plt.title(symbol)
plt.xlabel('Days (after ' + str(datetime.today()-relativedelta(days=len(series)))[:10] + ')')
plt.ylabel('Prices (current = $' + str(round(series.values[-1], 2)) + " USD)")
plt.plot(series, label=symbol)
plt.plot(support, label='Support', c='r')
plt.plot(resistance, label='Resistance', c='g')
plt.plot(current, label='Current', c='grey')
plt.legend()
plt.show()
