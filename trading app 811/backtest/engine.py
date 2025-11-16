import pandas as pd
import numpy as np
from utils.metrics import calculate_sharpe, calculate_drawdown

def run_backtest(data, initial_cash=10000):
    cash = initial_cash
    position = 0
    portfolio_values = []

    for i in range(len(data)):
        price = data.iloc[i]["Close"]
        signal = data.iloc[i]["signal"]

        # Buy if signal is 1 and no position
        if signal == 1 and position == 0:
            position = cash / price
            cash = 0

        # Sell if signal is 0 and holding position
        elif signal == 0 and position > 0:
            cash = position * price
            position = 0

        # Calculate current portfolio value
        portfolio_value = cash + position * price
        portfolio_values.append(portfolio_value)

    data["portfolio_value"] = portfolio_values
    data["strategy_returns"] = data["portfolio_value"].pct_change()

    # Calculate performance metrics
    sharpe = calculate_sharpe(data["strategy_returns"])
    drawdown = calculate_drawdown(data["portfolio_value"])

    results = {
        "final_value": data["portfolio_value"].iloc[-1],
        "sharpe_ratio": sharpe,
        "max_drawdown": drawdown,
        "data": data
    }

    return results

from backtest.engine import run_backtest

results = run_backtest(data_with_signals)
print("Final Portfolio Value:", results["final_value"])
print("Sharpe Ratio:", results["sharpe_ratio"])
print("Max Drawdown:", results["max_drawdown"])
