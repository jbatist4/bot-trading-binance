## Binance Trading Bot - Automated EMA Crossover Strategy
🚀 Automated Trading Bot for Binance using Python and the Exponential Moving Average (EMA) Crossover Strategy.

## Features  
  ✅ Fetches real-time BTC/USDT price from Binance  
  ✅ Implements EMA crossover (9-period and 21-period) for buy/sell signals  
  ✅ Supports stop-loss (2%) and take-profit (5%) for risk management  
  ✅ Fully automated trading with market orders  

## How It Works  
The bot continuously fetches price data and calculates the EMAs.  
It buys when the short EMA (9) crosses above the long EMA (21).  
It sells when the price reaches either the take-profit or stop-loss level.  

## Installation & Usage  
Clone the repository  
git clone https://github.com/jbatist4/bot-trading-binance.git    
cd bot-trading-binance  

## Install dependencies  
pip install ccxt numpy talib    

Add your Binance API keys inside the script.  
Run the bot  
python bot_trading_binance.py  

## ❤️Donations  
### If you find this bot useful, consider supporting the project with a donation:  
**BTC:** bc1qqh6hsh5q9lpxp2cs9ljlax5sxa456ctk2uj3qg  
**ETH:** 0xf4B8FC6a857F864DD0944bf2333E986ea8224AC5  
**SOL:** 8VDEqbz7yucGG6RWKEtEvRfxqYthn4cpkTJECQXY3EvX  
