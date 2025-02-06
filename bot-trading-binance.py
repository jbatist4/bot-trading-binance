import ccxt
import time
import logging
import talib
import numpy as np

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Binance API configuration
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

binance = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'options': {'defaultType': 'spot'},
})

# Trading pair and trade amount
TRADING_PAIR = "BTC/USDT"
TRADE_AMOUNT = 0.001  # Adjust as needed

# Risk management settings
STOP_LOSS_PERCENT = 2  # 2% stop-loss
TAKE_PROFIT_PERCENT = 5  # 5% take-profit
EMA_SHORT_PERIOD = 9
EMA_LONG_PERIOD = 21


def get_price():
    """Gets the current asset price."""
    ticker = binance.fetch_ticker(TRADING_PAIR)
    return ticker['last']

def get_historical_data():
    """Fetches historical data for the asset."""
    candles = binance.fetch_ohlcv(TRADING_PAIR, timeframe='1h', limit=50)
    return np.array([candle[4] for candle in candles], dtype=np.float64)

def calculate_ema():
    """Calculates exponential moving averages (EMA)."""
    prices = get_historical_data()
    ema_short = talib.EMA(prices, timeperiod=EMA_SHORT_PERIOD)[-1]
    ema_long = talib.EMA(prices, timeperiod=EMA_LONG_PERIOD)[-1]
    return ema_short, ema_long

def place_order(order_type, price=None):
    """Places a buy or sell order."""
    try:
        if order_type == "buy":
            order = binance.create_market_buy_order(TRADING_PAIR, TRADE_AMOUNT)
        else:
            order = binance.create_market_sell_order(TRADING_PAIR, TRADE_AMOUNT)
        logging.info(f"{order_type.upper()} order executed: {order}")
    except Exception as e:
        logging.error(f"Error executing order: {e}")

def trading_strategy():
    """EMA crossover-based trading strategy."""
    while True:
        ema_short, ema_long = calculate_ema()
        current_price = get_price()
        stop_loss = current_price * (1 - STOP_LOSS_PERCENT / 100)
        take_profit = current_price * (1 + TAKE_PROFIT_PERCENT / 100)
        
        if ema_short > ema_long:
            logging.info(f"EMA crossover detected! Buying {TRADING_PAIR} at {current_price} USDT")
            place_order("buy")
            
            while True:
                current_price = get_price()
                if current_price <= stop_loss or current_price >= take_profit:
                    logging.info(f"Condition met at {current_price} USDT. Selling...")
                    place_order("sell")
                    break
                time.sleep(10)
        time.sleep(60)

if __name__ == "__main__":
    trading_strategy()
