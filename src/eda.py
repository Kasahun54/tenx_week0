# src/eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, columns, title="Time Series Plot"):
    df.plot(x='Timestamp', y=columns, figsize=(10, 6))
    plt.title(title)
    plt.show()

def plot_correlation_matrix(df, columns, title="Correlation Matrix"):
    corr = df[columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()

def plot_missing_values(df, title="Missing Values"):
    missing_values = df.isnull().sum()
    plt.figure(figsize=(10, 6))  
    sns.barplot(x=missing_values.index, y=missing_values.values)
    plt.title(title)
    plt.show()

def plot_outliers(df, columns, title="Outliers"):
    for column in columns:  
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[column])
        plt.title(f"{title} for {column}")
        plt.show()

def plot_histogram(df, columns, title="Histogram"):
    for column in columns:  
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True)
        plt.title(f"{title} for {column}")
        plt.show()

def plot_scatter_matrix(df, columns, title="Scatter Matrix"):
    plt.figure(figsize=(10, 6))
    sns.pairplot(df[columns])
    plt.title(title)
    plt.show()

def calculate_statistics(df, column):
    stats = df[column].describe()
    return stats

def calculate_correlation(df, columns):
    corr = df[columns].corr()
    return corr
