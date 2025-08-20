import pandas as pd

def detect_entry(df):
    df['VWAP'] = (df['Volume'] * (df['High'] + df['Low'] + df['Close']) / 3).cumsum() / df['Volume'].cumsum()
    df['VolSpike'] = df['Volume'] > df['Volume'].rolling(20).mean() * 1.5
    df['Signal'] = (df['Close'] > df['VWAP']) & df['VolSpike']
    return df[df['Signal']]