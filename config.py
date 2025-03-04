from datetime import datetime

# Hardcoded API key
API_KEY = "19HMEFNX7EOOMTV4"

# Combined file path
COMBINED_FILE_PATH = "abfss://bronze@capitaledgestorage01.dfs.core.windows.net/combined.csv"

# Stock-specific configurations
STOCK_CONFIG = {
    "AAPL": {
        "base_url": "https://www.alphavantage.co/query",
        "params": {
            "function": "TIME_SERIES_DAILY",
            "symbol": "AAPL",
            "apikey": API_KEY,
            "datatype": "json",
        },
    },
    "GOOGL": {
        "base_url": "https://www.alphavantage.co/query",
        "params": {
            "function": "TIME_SERIES_DAILY",
            "symbol": "GOOGL",
            "apikey": API_KEY,
            "datatype": "json",
        },
    },
    "MSFT": {
        "base_url": "https://www.alphavantage.co/query",
        "params": {
            "function": "TIME_SERIES_DAILY",
            "symbol": "MSFT",
            "apikey": API_KEY,
            "datatype": "json",
        },
    },
}
