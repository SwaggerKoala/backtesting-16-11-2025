import pandas as pd

class BaseStrategy:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.data["signal"] = 0  # Default signal column

    def generate_signals(self):
        raise NotImplementedError("You must implement generate_signals() in your strategy.")
