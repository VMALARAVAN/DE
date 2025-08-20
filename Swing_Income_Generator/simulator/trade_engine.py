import random

def simulate_trade(entry_price, atr, sl_factor, target_factor, brokerage):
    sl = entry_price - atr * sl_factor
    target = entry_price + atr * target_factor
    outcome = random.choices(['target', 'sl'], weights=[0.65, 0.35])[0]
    exit_price = target if outcome == 'target' else sl
    pnl = exit_price - entry_price
    net_pnl = pnl - brokerage
    return round(net_pnl, 2), outcome