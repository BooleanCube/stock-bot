import yfinance as yf
import matplotlib.pyplot as plt
from utility.linear_regression import *
from utility.curve_fitting import *
from utility.graph_analysis import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib


matplotlib.use("TkAgg")

symbol = input("Please input a correct stock symbol: ")
df = yf.download(symbol, start=datetime.today()-relativedelta(months=6), end=datetime.today())

series = df['Close'].squeeze()
series.index = np.arange(len(series))

month_diff = series.shape[0] // 30
if month_diff == 0:
    month_diff = 1

smooth = int(2 * month_diff + 3)

pts = savitzky_golay_filter(series.to_numpy(), smooth, 3)

relative_min, relative_max = relative_min_max(pts)

relative_min_slope, relative_min_int = linear_regression(relative_min)
relative_max_slope, relative_max_int = linear_regression(relative_max)

index_array = series.index
support = (relative_min_slope * index_array) + relative_min_int
resistance = (relative_max_slope * index_array) + relative_max_int
current = (0 * index_array) + series.values[-1]

plt.title(symbol)
plt.xlabel('Days (after ' + str(datetime.today()-relativedelta(days=len(series)))[:10] + ')')
plt.ylabel('Prices (current = $' + str(round(series.values[-1], 2)) + " USD)")
plt.plot(index_array, series, label=symbol)
plt.plot(index_array, support, label='Support', c='r')
plt.plot(index_array, resistance, label='Resistance', c='g')
plt.plot(index_array, current, label='Current', c='grey')
plt.legend()
plt.show()
