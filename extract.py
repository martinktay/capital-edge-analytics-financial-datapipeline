import requests
import time


def fetch_api_data(base_url, params):
    """
    Fetches data from the API.
    """
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed for {params['symbol']}: {e}")
    return response.json()


def validate_api_response(data, key):
    """
    Validates the API response to ensure it contains the expected data.
    """
    if key not in data:
        if "Note" in data:
            raise Exception("API rate limit exceeded. Try again later.")
        if "Error Message" in data:
            raise Exception(f"API error: {data['Error Message']}")
        raise Exception(f"Unexpected API response: {data}")
    return data[key]


def extract_stock_data(stock_config):
    """
    Extracts stock data for all configured stocks.
    """
    stock_data = {}
    for symbol, config in stock_config.items():
        print(f"Fetching data for symbol: {symbol}")
        time.sleep(12)  # Adhere to API rate limits
        raw_data = fetch_api_data(config["base_url"], config["params"])
        stock_data[symbol] = validate_api_response(raw_data, "Time Series (Daily)")
    return stock_data
