def check_signal(pair):
    # TEST MODE - kirim 1 sinyal contoh
    if pair == "XAUUSD":
        return f"""
📊 PAIR: {pair}
📈 SIGNAL: BUY
🎯 ENTRY: 2320 - 2323
🛑 SL: 2312
✅ TP1: 2330
✅ TP2: 2342
📐 RR: 1:2.5
📊 CONFIDENCE: 80%
⏰ TF: M5 + H1
"""
    return None
