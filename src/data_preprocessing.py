# src/eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, columns, title="Time Series Plot"):
    df.plot(x='Timestamp', y=columns, figsize=(10, 6))
    plt.title(title)
    plt.show()
