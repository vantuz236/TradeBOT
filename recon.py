import requests

SYMBOL = 'BTCUSDT'
INTERVAL = "1d"

DAY_LIMIT = 60
HOUR_LIMIT = 24
MENUTE_LIMIT = 60

def get_bars(symbol, interval, limit):
    url = "https://api.binance.com/api/v3/klines"
    curr_params = {"symbol": symbol, "interval": interval, "limit": limit}

    response = requests.get(url, params = curr_params)
    raw_data = response.json()
    bars = []

    for item in raw_data:
        bar = {
            "time": item[0],
            "open": float(item[1]),
            "high": float(item[2]),
            "low": float(item[3]),
            "close": float(item[4]),
            "volume": float(item[5])
        }
        bars.append(bar)

    return bars

def get_all_frames(symbol=SYMBOL):
    frames = {
        "d": get_bars(symbol, "1d", DAY_LIMIT),
        "h": get_bars(symbol, "1h", HOUR_LIMIT),
        "m": get_bars(symbol, "1m", MENUTE_LIMIT)
    }
    return frames