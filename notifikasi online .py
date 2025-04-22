import requests
import time
import telegram

# Ganti dengan token bot Telegram lo
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"  # Ganti dengan chat ID lo

# URL API Indodax
url = "https://api.indodax.com/ticker/{pair}.json"  # Misalnya: ticker/btcidr

# Fungsi untuk ngirim notifikasi
def send_notification(message):
    bot.send_message(chat_id=chat_id, text=message)

# Fungsi untuk ngecek perubahan harga
def check_price(pair):
    prev_price = None
    while True:
        response = requests.get(url.format(pair=pair))
        data = response.json()
        
        # Ambil harga terakhir
        current_price = data['ticker']['last']
        
        if prev_price:
            # Hitung persentase perubahan
            percentage_change = ((current_price - prev_price) / prev_price) * 100
            
            # Cek jika perubahan lebih dari 10%
            if percentage_change >= 10:
                message = f"Coin {pair} naik lebih dari 10%! Harga: {current_price}"
                send_notification(message)
        
        prev_price = current_price
        time.sleep(300)  # Tunggu 5 menit (300 detik)

# Pilih pair yang lo mau pantau, misalnya BTC/IDR
check_price("btc_idr")