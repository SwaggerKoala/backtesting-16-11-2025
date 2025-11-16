import streamlit as st
import pandas as pd
from data.fetcher import get_data
from strategies.moving_average import MovingAverageStrategy
from backtest.engine import run_backtest
from ui.plots import plot_candlestick_with_signals, plot_equity_curve

st.set_page_config(page_title="Quant Trading Dashboard", layout="wide")

st.title("📈 Quant Trading Dashboard")

# Sidebar inputs
symbol = st.sidebar.text_input("Enter Asset Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
short_window = st.sidebar.slider("Short MA Window", 5, 50, 20)
long_window = st.sidebar.slider("Long MA Window", 20, 200, 50)

if st.sidebar.button("Run Strategy"):
    # Fetch and process data
    data = get_data(symbol, str(start_date), str(end_date))
    strategy = MovingAverageStrategy(data, short_window, long_window)
    enriched_data = strategy.generate_signals()
    results = run_backtest(enriched_data)

    st.subheader("Candlestick Chart with Signals")
    plot_candlestick_with_signals(results["data"])

    st.subheader("Equity Curve")
    plot_equity_curve(results["data"])

    st.metric("Final Portfolio Value", f"${results['final_value']:,.2f}")
    st.metric("Sharpe Ratio", results["sharpe_ratio"])
    st.metric("Max Drawdown", f"{results['max_drawdown']*100:.2f}%")

