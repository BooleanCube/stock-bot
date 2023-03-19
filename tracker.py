from pandas_datareader import data as pdr
import yfinance as yf
import time
from utility.linear_regression import *
from utility.curve_fitting import *
from utility.graph_analysis import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from getpass import getpass
import smtplib
import ssl
import sys


"""
CONFIGURABLE STATIC VARIABLES
Please configure your setup correctly or else the tracker 
will not be able to send notifications and track correct companies!
(You must generate a Google Apps Password)
"""
email = "my@gmail.com" # make sure to input a valid email address (you will receive notifications here)
default_password = "password" # put password here to store it, instead of having to input everytime
tickers = ["LIST", "OF", "STOCKS", "TO", "TRACK"] # make sure the stock tickers are valid (eg. AAPL or NFLX)
error_constant = 0.03 # 3% error in support and resistance calculations
timeout = 3600 # timeout duration in seconds
ppps = 3000 # Preferable Profit Per Stock (PPPS in dollars)
plps = 400 # Preferable Loss Per Stock (PLPS in dollars)
limit_risk = False # Set strict limits to the amount of loss you are willing to make (less risk, less gain)


# input the Google Apps (16-Digit) Password generated under a "MAIL" application and a "CUSTOM" device.
password = getpass("Type your password and press enter: ", sys.stdout) if default_password == "password" else default_password
port = 465 # For SSL
yf.pdr_override()

context = ssl.create_default_context()

def send_email(sender, receiver, subject, message):
    body = "Subject: " + subject + "\n\n\n" + message
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(sender, receiver, body)


investments = set()

while True:
    for stock in tickers:
        symbol = stock
        df = pdr.get_data_yahoo(symbol, datetime.today() - relativedelta(months=8), datetime.today())
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

        current_price = series.values[-1]
        error_scope = current_price * error_constant # percent error from the current price of the stock
        shares = round(ppps / (resistance[-1]-error_scope - current_price), 4)
        lower_limit = round(current_price - plps / shares, 2) if limit_risk else round(support[-1] - plps / shares, 2)
        upper_limit = round(resistance[-1] + plps / shares, 2)

        # Skip or Sell stocks with crossing resistance and support lines. (Unpredictable stock prices aren't safe to invest in)
        if support[-1] > resistance[-1] and stock not in investments:
            continue
        elif support[-1] > resistance[-1] and stock in investments:
            investments.remove(stock)
            send_email(
                email,
                email,
                "[SELL] Stock-Bot Notification",
                stock + " has reached within a 5% error of the resistance regression line.\n"
                        "I suggest selling all shares in " + stock + " ASAP!\n"
            )
            continue

        if resistance[-1] - error_scope <= current_price and stock in investments :
            investments.remove(stock)
            send_email(
                email,
                email,
                "[SELL] Stock-Bot Notification",
                stock + " has reached within a 5% error of the resistance regression line.\n"
                    "I suggest selling all shares in " + stock + " ASAP!\n"
                    "However, I recommend taking a look at the news around it first because there is a chance that it will sky rocket even further!"
            )
        elif support[-1] + error_scope >= current_price and stock not in investments:
            investments.add(stock)
            send_email(
                email,
                email,
                "[BUY] Stock-Bot Notification",
                stock + " has reached within a 5% error of the support regression line.\n"
                    "I suggest investing in " + stock + " ASAP!\n"
                    "Recommended # of Shares ~ " + str(shares) + "\n"
                    "Recommended Buy Limit ~ $" + str(lower_limit).zfill(2) + " USD\n"
                    "Recommended Sell Limit ~ $" + str(upper_limit).zfill(2) + " USD\n"
                    "However, I recommend taking a look at the news around it first because it may be crashing from unfortunate circumstances!"
            )

    # update statuses again in *timeout* seconds
    time.sleep(timeout)
