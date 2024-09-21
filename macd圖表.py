import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載台積電股票數據 (代碼: 2330.TW)
tsmc = yf.Ticker("2330.TW")

# 抓取2023年的股價數據
data = tsmc.history(start="2023-01-01", end="2023-12-31")

# 計算12日和26日的指數移動平均線 (EMA)
data['12_EMA'] = data['Close'].ewm(span=12, adjust=False).mean()
data['26_EMA'] = data['Close'].ewm(span=26, adjust=False).mean()

# 計算MACD線
data['MACD'] = data['12_EMA'] - data['26_EMA']

# 計算訊號線 (9日EMA)
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

# 計算MACD柱狀圖 (MACD - 訊號線)
data['MACD_Histogram'] = data['MACD'] - data['Signal_Line']

# 繪製MACD圖表
plt.figure(figsize=(12,8))

# 繪製收盤價圖表
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.title('TSMC 2023 Closing Price and MACD')
plt.xlabel('Date')
plt.ylabel('Price (TWD)')
plt.grid(True)
plt.legend()

# 繪製MACD和訊號線圖表
plt.subplot(2, 1, 2)
plt.plot(data.index, data['MACD'], label='MACD', color='green')
plt.plot(data.index, data['Signal_Line'], label='Signal Line', color='red')
plt.bar(data.index, data['MACD_Histogram'], label='MACD Histogram', color='blue')
plt.xlabel('Date')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()