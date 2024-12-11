import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.eda import (
    plot_time_series,
    plot_correlation_matrix,
    plot_missing_values,
    plot_outliers,
    plot_histogram,
    calculate_statistics,
)

def load_data(filepath="notebooks/data/togo-dapaong_qc.csv"):
    try:
        df = pd.read_csv(filepath)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}. Please check the path.")
        return pd.DataFrame()

if __name__ == "__main__":
    data = load_data()

    if not data.empty:
        plot_time_series(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Time Series of Solar Data")
        plot_correlation_matrix(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Correlation Matrix")
        plot_missing_values(data, title="Missing Values in Solar Data")
        plot_outliers(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Outliers in Solar Data")
        plot_histogram(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Histogram of Solar Data")
    else:
        print("Dataset is empty. Please check the file.")

    print(calculate_statistics(data, 'GHI'))
