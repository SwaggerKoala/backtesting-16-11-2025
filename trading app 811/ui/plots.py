import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_candlestick_with_signals(data, title="Candlestick Chart"):
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot candlesticks
    ax.plot(data["timestamp"], data["Close"], label="Close Price", color="black")

    # Plot buy signals
    buy_signals = data[data["signal"] == 1]
    ax.scatter(buy_signals["timestamp"], buy_signals["Close"], label="Buy", color="green", marker="^")

    # Plot sell signals
    sell_signals = data[data["signal"] == 0]
    ax.scatter(sell_signals["timestamp"], sell_signals["Close"], label="Sell", color="red", marker="v")

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_equity_curve(data, title="Equity Curve"):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data["timestamp"], data["portfolio_value"], label="Portfolio Value", color="blue")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

from ui.plots import plot_candlestick_with_signals, plot_equity_curve

plot_candlestick_with_signals(results["data"])
plot_equity_curve(results["data"])
