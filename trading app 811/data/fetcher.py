# 1. Import necessary libraries
import yfinance as yf               # To fetch financial data from Yahoo Finance
import pandas as pd                 # For data manipulation and analysis
import numpy as np                  # For numerical operations
import os                           # To handle file paths

# 2. Define the main function to fetch and process data
def get_data(symbol, start_date, end_date, save_csv=True):
    # 3. Download historical data using yfinance
    df = yf.download(symbol, start=start_date, end=end_date)
    # 4. Add a timestamp column from the index
    df.reset_index(inplace=True)
    df.rename(columns={"Date": "timestamp"}, inplace=True)
    # 5. Add log returns
    df["returns"] = np.log(df["Close"] / df["Close"].shift(1))
    # 6. Add rolling volatility (20-day standard deviation of returns)
    df["volatility"] = df["returns"].rolling(window=20).std()
    # 7. Add a placeholder for strategy signals (to be filled later)
    df["signal"] = 0
    # 8. Add asset symbol as a column
    df["asset"] = symbol
    # 9. Drop rows with missing values (from rolling calculations)
    df.dropna(inplace=True)
    # 9. Drop rows with missing values (from rolling calculations)
    df.dropna(inplace=True)
    # 10. Save to CSV if requested
    if save_csv:
        os.makedirs("data", exist_ok=True)  # Create data folder if it doesn't exist
        file_path = f"data/{symbol}.csv"
        df.to_csv(file_path, index=False)
        print(f"Saved data to {file_path}")
    # 11. Return the DataFrame for use in other modules
    return df
