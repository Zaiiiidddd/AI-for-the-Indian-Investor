AI Investor – Stock Signal Engine

AI Investor is a Python-based stock analysis tool that helps interpret market data and generate simple trading signals. The goal of this project is to move beyond raw numbers and provide meaningful insights that are easier to understand.

The system fetches real-time stock data and applies basic technical analysis to detect patterns such as breakouts, trends, and unusual volume activity. Each signal is accompanied by a short explanation and a confidence score. A backtesting function is included to estimate how similar signals have performed historically.

This project is intentionally kept lightweight and easy to run, making it suitable for learning purposes as well as a base for more advanced financial applications.

Features
Real-time stock data using yfinance
Detection of breakout, trend, and volume-based signals
Moving average-based trend analysis
Historical backtesting for signal evaluation
FastAPI-based API for quick access
Tech Stack
Python
FastAPI
pandas
yfinance
Setup

Install dependencies:

pip install fastapi uvicorn yfinance pandas

Run the project:

python main.py
Usage

Once the server is running, open your browser and use:

http://127.0.0.1:8000/analyze/RELIANCE

You can replace the stock symbol with any NSE-listed stock.

Example Output
{
  "stock": "RELIANCE",
  "current_price": 2850.5,
  "signal": "Bullish Breakout",
  "reason": "Stock is near 3-month high indicating strong upward momentum",
  "confidence": 80,
  "pattern": "Strong Uptrend",
  "historical_accuracy": "72.5%"
}
