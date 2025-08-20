import pandas as pd

def monthly_projection(trades):
    df = pd.DataFrame(trades)
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
    summary = df.groupby('Month')['Net_PnL'].sum().reset_index()
    return summary