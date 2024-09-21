import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載台積電股票數據 (台積電代碼: 2330.TW)
tsmc = yf.Ticker("2330.TW")

# 抓取2023年的股價數據
data = tsmc.history(start="2023-01-01", end="2023-12-31")

# 計算每日的價格變動
delta = data['Close'].diff()

# 將上漲和下跌分開
gain = (delta.where(delta > 0, 0))
loss = (-delta.where(delta < 0, 0))

# 計算14天的平均上漲和下跌
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()

# 計算相對強弱 (RS)
rs = avg_gain / avg_loss

# 計算 RSI
data['RSI'] = 100 - (100 / (1 + rs))

# 繪製 RSI 圖表
plt.figure(figsize=(12,6))
plt.plot(data.index, data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.title('TSMC 2023 RSI (Relative Strength Index)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.grid(True)
plt.show()
