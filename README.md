# stock-bot
> Stock trading algorithms using trend-based statistics for the trading bots in the stock market.

## DISCLAIMER
I am not responsible for any profits or losses you receive. Please use this responsibly. I don't suggest using this without knowing how it works. Be careful with your investments and don't blindly trust the stock tracker.

## Support-Resistance Stock Trading Model
The support and resistance trading strategy is one of the most common and legitimate trading strategies. We analyze the company by performing statistical analysis of that company's previous stock price history. If we analyze only the last 5 months, results will usually appear in around 1-2 months time. The larger the period of history analyzed, the more precise the predictions will be.
<br>
### Explanation
Stock prices are chaotic. (If you haven't checked my [chaos theory research](https://github.com/BooleanCube/chaos-theory), check it out)<br>
They fluctuate between relative minimum and maximum values as it moves ahead. The goal behind the support-resistance strategy is to buy at a relative minimum and sell at a relative maximum and maximize our profits.

In our model, we will base our moves on 2 different lines which we will calculate: the support line and the resistance line.<br>
The support line is a generated linear regression line of all the relative minimums on the graph of the stock price history.<br>
Similarly, the resistance line is a generated linear regression line of all the relative maximums on the graph of the stock price history.<br>
*A regression line is used to predict the commonly trending pattern in the relative extrema of the graph.*

![image](https://user-images.githubusercontent.com/47650058/226204947-c96ee5c0-058d-4854-b0b7-c98ac2ec118f.png)

### Optimization
Since, the stock prices can be very flicky and finnicky, finding the relative minimums and maximums of an unfiltered stock price graph would be very slow. So, after conducting some research, I learned that using a savitzky golay smoothening filter is the best way to smoothen a stock history graph without losing too much precision.<br>
Learn more about the Savitzky Golay Filter here: https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter

### Strategy
The strategy is to buy when the stock price reaches within a error scope of the support line prediction and to sell when the stock price reaches within the error scope of the resistance line prediction. The tracker script, tracks stock prices every 5 minutes for these 2 events and once triggered, will send you an email notification.

#### Advice
- Check the news before trusting any of the tracker's advice, because even though a stock reaches a support prediction, the truth may be that the company is going bankrupt or even crashing.
- If support and resistance lines cross each other, I wouldn't trust the stock because that means the history was too unpredictable.
- If the support and resistance predictions are too close to each other, I wouldn't suggest investing in that company either because profits aren't that large.

#### Example
An example of a good time to buy a good stock would be:<br><br>
![image](https://user-images.githubusercontent.com/47650058/226205871-10c392ba-4123-429c-833e-9976716b71f1.png)<br>
*NFLX Stock at 4:00PM on 03/19/2023*<br><br>

The stock seems to be stable, and there is no apparent news about crashing. The stock price is near the support predictions and there is a large gap between the support prediction and the resistance prediction. This means, that if the NFLX stock reaches the predicted relative maximum, then profits will also be very large.

#### Proof
Just 4 days into testing, and I have already made slightly over $2000 USD.
![image](https://user-images.githubusercontent.com/47650058/226206146-f3564f15-fd59-4a98-b22f-69b85ce98b39.png)

## Analyze Stock
The `analyze_stock.py` script allows a user to graph, visualize and analyze specific stock price histories. Multiple examples of the visualization have been shown above.
<br><br>
Analyzing stocks is very important because you want to be able to expand your investments as large as you can and invest in as many companies as possible to maximize your profits.
<br><br>
Use this script to analyze stocks and pick companies that you want to be able to invest in the future. This utility will come useful if you apply the advice I have listed above. Try to find stocks with stable price history. If companies have approximately parallel support and resistance lines, it shows signs of stability and is the least risky way to gain profit. The best case scenario would be to have parallel support and resistance lines that have a good amount of distance from each other so you can make some good profit.

## Stock Tracker Bot
The `tracker.py` script runs a program that will constantly track stock prices periodically. This program can be run on a server 24/7 and will constantly notify you on when to invest or sell for maximum profit.

### Google App Password
**Your regular gmail password won't work for this.**
You need to generate a google apps password, if you haven't already.<br>
1. Go to your [google account portal](https://myaccount.google.com/)
2. Click on the "Search Google Account" search bar and search for "App passwords" and click on it
3. Under "Select App", choose "Mail" and under "Select Device", choose "Other *(custom name)*" and name your device as anything such as "Computer".
4. Click "Generate" and copy the password.
5. Save the password somewhere because you might not be able to access it again.

This is the password you will be using to connect the stock bot to your gmail.

### Configurable Constants
- `email`: Gmail account you want to send notifications to. (REQUIRED)
- `default_password`: Include your password here if you don't want to input password secretly everytime. To input everytime secretly, set it to "password" by dafault. (OPTIONAL)
- `error_constant`: Specify the error scope you would like to use when checking stock prices with support and resistance predictions. (**3%** by default)
- `timeout`: Specify the amount of time between each periodical check. (**1 hour** by default)
- `ppps`: Specify the preferable amount of profit per stock you would like to make using this bot. (**$3000 USD** by default)
- `plps`: Specify the preferable amount of loss per stock you would like to have using this bot. (**$400 USD** by default)
- `limit_risk`: Specify whether you would like strict limits on the amount of loss you are willing to make per stock. It will not make more than `plps` loss per stock. (**False** by dafault)

## Usage

### Prerequisites
Make sure you have [python3 with pip]() installed. Also have [git](https://git-scm.com/downloads) installed, or else download the zip file from the latest release in the [releases page](https://github.com/BooleanCube/stock-bot/releases).
<br><br>
To be able to run all scripts, first you need to download this project and install all prerequisite Python packages:
```console
$ git clone https://github.com/BooleanCube/stock-bot.git
$ cd stock-bot/
$ pip install -r requirements.txt
```

### Analyze Stock History Graphs
You can run the `analyze_stock.py` script by using this command:
```console
$ python3 analyze_stock.py
```
and then inputting the ticker of the company you want to graph using the script.
<br>

### Stock Tracker Notification Bot
You can start the stock bot by running this command in a terminal (suggest to not run this within IDE consoles)
```console
$ python3 tracker.py
```
and then input the dedicated google app password for the stock bot (if not already set as the `default_password`)

----

*Created by BooleanCube :]*
