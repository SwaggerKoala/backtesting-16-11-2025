import numpy as np


def calculate_sharpe(returns, risk_free_rate=0.0):
    """
    Calculates the Sharpe ratio.
    returns: Series of strategy returns
    risk_free_rate: Annual risk-free rate (default 0.0)
    """
    excess_returns = returns - risk_free_rate / 252  # Convert annual rate to daily
    mean = excess_returns.mean()
    std = excess_returns.std()
    sharpe_ratio = mean / std if std != 0 else 0
    return round(sharpe_ratio, 3)

def calculate_drawdown(portfolio_values):
    """
    Calculates maximum drawdown.
    portfolio_values: Series of portfolio values over time
    """
    cumulative_max = portfolio_values.cummax()
    drawdowns = (portfolio_values - cumulative_max) / cumulative_max
    max_drawdown = drawdowns.min()
    return round(max_drawdown, 3)

from utils.metrics import calculate_sharpe, calculate_drawdown

sharpe = calculate_sharpe(data["strategy_returns"])
drawdown = calculate_drawdown(data["portfolio_value"])
