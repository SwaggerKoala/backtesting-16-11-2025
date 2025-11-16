from data.fetcher import get_data
from strategies.moving_average import MovingAverageStrategy

data = get_data("AAPL", "2022-01-01", "2023-01-01")
strategy = MovingAverageStrategy(data)
data_with_signals = strategy.generate_signals()
print(data_with_signals[["timestamp", "Close", "ma_short", "ma_long", "signal"]].tail())
