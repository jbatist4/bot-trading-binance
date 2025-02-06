import ccxt
import talib
import numpy as np

def fetch_historical_data(exchange, trading_pair, timeframe='1h', limit=50):
    candles = exchange.fetch_ohlcv(trading_pair, timeframe=timeframe, limit=limit)
    return np.array([candle[4] for candle in candles], dtype=np.float64)

def calculate_ema(prices, short_period=9, long_period=21):
    ema_short = talib.EMA(prices, timeperiod=short_period)[-1]
    ema_long = talib.EMA(prices, timeperiod=long_period)[-1]
    return ema_short, ema_long
