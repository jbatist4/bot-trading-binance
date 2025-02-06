import time
import logging
from src.utils import fetch_historical_data, calculate_ema

def trading_strategy(exchange, trading_pair, stop_loss_percent, take_profit_percent):
    while True:
        prices = fetch_historical_data(exchange, trading_pair)
        ema_short, ema_long = calculate_ema(prices)
        logging.info(f"EMA Short: {ema_short}, EMA Long: {ema_long}")

        if ema_short > ema_long:
            logging.info(f"EMA crossover detected! Buying {trading_pair}.")
            # Adicionar função para executar a ordem
            # Implementar stop-loss e take-profit
        time.sleep(60)
