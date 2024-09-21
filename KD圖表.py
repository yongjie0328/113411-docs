import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載台積電股票數據 (代碼: 2330.TW)
tsmc = yf.Ticker("2330.TW")

# 抓取2023年的股價數據
data = tsmc.history(start="2023-01-01", end="2023-12-31")

# 計算9日內的最高價和最低價
low_9 = data['Low'].rolling(window=9).min()
high_9 = data['High'].rolling(window=9).max()

# 計算K值 (隨機指標)
data['K'] = (data['Close'] - low_9) / (high_9 - low_9) * 100

# 計算D值 (K值的3日移動平均)
data['D'] = data['K'].rolling(window=3).mean()

# 繪製KD指標圖表
plt.figure(figsize=(12,6))
plt.plot(data.index, data['K'], label='%K', color='blue')
plt.plot(data.index, data['D'], label='%D', color='red')
plt.title('TSMC 2023 KD Indicator')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
