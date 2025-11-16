from strategies.base_strategy import BaseStrategy

class MovingAverageStrategy(BaseStrategy):
    def __init__(self, data, short_window=20, long_window=50):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        self.data["ma_short"] = self.data["Close"].rolling(window=self.short_window).mean()
        self.data["ma_long"] = self.data["Close"].rolling(window=self.long_window).mean()

        # Buy signal when short MA crosses above long MA
        self.data["signal"] = (self.data["ma_short"] > self.data["ma_long"]).astype(int)

        return self.data
