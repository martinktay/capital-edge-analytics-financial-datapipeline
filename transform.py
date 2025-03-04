def parse_time_series_data(time_series, symbol, existing_dates):
    """
    Transforms raw time series data into a list of dictionaries.
    """
    parsed_data = []
    for date, metrics in time_series.items():
        if date in existing_dates:
            continue  # Skip dates that are already in the file
        parsed_data.append({
            "Date": date,
            "Open": metrics["1. open"],
            "High": metrics["2. high"],
            "Low": metrics["3. low"],
            "Close": metrics["4. close"],
            "Volume": metrics["5. volume"],
            "Symbol": symbol,
        })
    return parsed_data
