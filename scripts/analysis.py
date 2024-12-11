import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
def load_data(filepath="notebooks/data/benin-malanville.csv"):
    try:
        df = pd.read_csv(filepath)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Parse timestamp
        print("Data loaded successfully!")
        print(df.info())
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}. Please check the path!")
        return pd.DataFrame()

# Plot time series for selected columns
def plot_time_series(df, columns):
    for column in columns:
        if column in df.columns:
            plt.plot(df['Timestamp'], df[column], label=column)
    plt.legend()
    plt.title("Time Series Analysis")
    plt.xlabel("Timestamp")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    df = load_data()

    # Check if data is non-empty
    if not df.empty:
        # Plot time series
        plot_time_series(df, ['GHI', 'DNI', 'DHI', 'Tamb'])
    else:
        print("Dataset is empty. Please check the file!")
