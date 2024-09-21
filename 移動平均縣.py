import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載台積電股票數據 (台積電代碼: 2330.TW)
tsmc = yf.Ticker("2330.TW")

# 抓取2023年的股價數據
data = tsmc.history(start="2023-01-01", end="2023-12-31")

# 計算30日移動平均線
data['30_MA'] = data['Close'].rolling(window=30).mean()

# 繪製股價和30日移動平均線圖表
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.plot(data.index, data['30_MA'], label='30-Day MA', color='red')
plt.title('TSMC 2023 Closing Price and 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (TWD)')
plt.legend()
plt.grid(True)
plt.show()
