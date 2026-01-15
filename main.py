import time
from telegram_sender import send_message
from strategy import check_signal

PAIRS = ["EURUSD", "XAUUSD", "BTCUSD"]

def run():
    for pair in PAIRS:
        signal = check_signal(pair)
        if signal:
            send_message(signal)

if __name__ == "__main__":
    while True:
        try:
            run()
            time.sleep(300)  # 5 menit
        except Exception as e:
            print("Error:", e)
            time.sleep(60)
