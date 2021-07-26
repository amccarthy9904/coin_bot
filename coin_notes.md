# coin boi

## Intro to TensorFlow
Good [article](https://towardsdatascience.com/introduction-to-tensorflow-ac1cc204d547)
, describes difference between sequential and Functional Models

## Input

Kraken API - good current OHLC data, not good historical

[Yahoo_finance](https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD) - daily historical data 2014
[Investing.com] (https://www.investing.com/crypto/bitcoin/historical-data)  - goes back further 2010

input last 50 days OHLC data


## Dataset

1 Build
using [Yahoo_finance](https://finance.yahoo.com/quote/BTC-USD/history?period1=1410825600&period2=1627084800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true)
stored in BTC-USD_orig.csv
removed 4 rows with nulls
use alter_data.py to create BTC-USD.csv, same data but remove date and adj close

2 Figure out how tensorflow wants it
[load_data_csv_tutorial] (https://www.tensorflow.org/tutorials/load_data/csv)

in alter_data.py
create 2d numpy array inputs
each ind of array will be an input to the model
inputs = ind 0 = [(yesterday) O,H,L,C,V, (day before yesterday) O,H,L,C,V, ... x48]
create numpy array labels
labels = ind 0 = [0 or 1 (price up or down for today)]




3 figure out how to use it to train

## Model

Sequential - basic model - each layer talks to the next, one output

Functional - advanced model:
    - Information flow through the model is non-linear (i.e., not sequential).
    - Layers need multiple inputs and/or outputs.
    - The model uses multiple inputs and/or outputs.
    - We need to use layer sharing.

Starting with Sequential, might need to use functional for full bot

### Layers
#### Input
50 previous days of OHLCV (Open, High, Low, Close, Volume) data
Order matters, no dates given
50 rows of CSV * 5 datapoints per row = 250 input nodes

#### Interior Layers
Not sure how these should be laid out


#### Output Layer
One Node 0 or 1
if 0 next day will be red
if 1 next day will be green
green means next days close > open






## Future iterations
maybe look at Coinbase API
[this](https://github.com/gdemos01/crypto-trading-ai-bot-basic) prject uses it [here](https://github.com/gdemos01/crypto-trading-ai-bot-basic/blob/master/CoinbaseAPI.py)


