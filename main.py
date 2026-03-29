
# AI INVESTOR - SINGLE FILE PROJECT
import yfinance as yf
import pandas as pd
from fastapi import FastAPI
import uvicorn

app = FastAPI()


# DATA FETCHING
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="3mo")
        return df
    except:
        return pd.DataFrame()



# SIGNAL ENGINE (CORE LOGIC)
def generate_signal(df):
    latest = df.iloc[-1]

    high_3m = df['Close'].max()
    avg_volume = df['Volume'].mean()

    # Breakout Detection
    if latest['Close'] >= high_3m * 0.98:
        return {
            "type": "Bullish Breakout",
            "confidence": 80,
            "reason": "Stock is near 3-month high indicating strong upward momentum"
        }

    # Volume Spike Detection
    elif latest['Volume'] > avg_volume * 2:
        return {
            "type": "High Volume Activity",
            "confidence": 65,
            "reason": "Unusual volume spike detected, possible institutional activity"
        }

    # Bearish Signal
    elif latest['Close'] < df['Close'].rolling(20).mean().iloc[-1]:
        return {
            "type": "Bearish Trend",
            "confidence": 60,
            "reason": "Price below 20-day moving average"
        }

    # Neutral
    else:
        return {
            "type": "Neutral",
            "confidence": 40,
            "reason": "No strong trading signal detected"
        }



# PATTERN DETECTION
def detect_pattern(df):
    ma20 = df['Close'].rolling(20).mean().iloc[-1]
    ma50 = df['Close'].rolling(50).mean().iloc[-1]

    if df['Close'].iloc[-1] > ma20 > ma50:
        return "Strong Uptrend"
    elif df['Close'].iloc[-1] < ma20 < ma50:
        return "Strong Downtrend"
    elif df['Close'].iloc[-1] > ma20:
        return "Weak Uptrend"
    else:
        return "Sideways / Weak Trend"



# BACKTESTING ENGINE
def backtest(df):
    success = 0
    total = 0

    for i in range(50, len(df) - 5):
        price = df['Close'][i]
        past_max = df['Close'][:i].max()

        if price >= past_max * 0.98:
            total += 1
            future_price = df['Close'][i + 5]

            if future_price > price:
                success += 1

    if total == 0:
        return 0

    return round((success / total) * 100, 2)



# MAIN ANALYSIS FUNCTION
def analyze(symbol):
    df = get_stock_data(symbol + ".NS")

    if df.empty:
        return {"error": "Invalid stock symbol"}

    signal = generate_signal(df)
    pattern = detect_pattern(df)
    accuracy = backtest(df)

    result = {
        "stock": symbol.upper(),
        "current_price": round(df['Close'].iloc[-1], 2),
        "signal": signal["type"],
        "reason": signal["reason"],
        "confidence": signal["confidence"],
        "pattern": pattern,
        "historical_accuracy": f"{accuracy}%"
    }

    return result



# API ROUTES
@app.get("/")
def home():
    return {"message": "AI Investor API Running"}


@app.get("/analyze/{symbol}")
def analyze_stock(symbol: str):
    return analyze(symbol)



# RUN SERVER
if _name_ == "_main_":
    print("\nAI INVESTOR STARTED")
    print("Open in browser:")
    print("http://127.0.0.1:8000/analyze/RELIANCE")
    print("http://127.0.0.1:8000/analyze/TCS\n")

    uvicorn.run(app, host="127.0.0.1", port=8000)
