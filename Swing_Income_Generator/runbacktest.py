import pandas as pd
import yaml
from strategy.vwap_breakout import detect_entry
from simulator.trade_engine import simulate_trade
from simulator.income_projection import monthly_projection

with open('config/settings.yaml') as f:
    config = yaml.safe_load(f)

trades = []

for symbol in config['symbols']:
    df = pd.read_csv(f'data/historical/{symbol}.csv')
    signals = detect_entry(df)

    for _, row in signals.iterrows():
        entry = row['Close']
        atr = row['High'] - row['Low']
        net_pnl, outcome = simulate_trade(entry, atr,
                                          config['sl_factor'],
                                          config['target_factor'],
                                          config['brokerage'])
        trades.append({
            'Date': row['Date'],
            'Symbol': symbol,
            'Entry': entry,
            'Outcome': outcome,
            'Net_PnL': net_pnl
        })

summary = monthly_projection(trades)
summary.to_csv('results/monthly_report.csv', index=False)
print(summary)