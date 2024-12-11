def clean_data(df):
    df = df.dropna(subset=['GHI', 'DNI', 'DHI'])
    df = df[df['GHI'] >= 0]  # Remove negative solar radiation values
    return df
