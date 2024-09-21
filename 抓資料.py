import yfinance as yf
import pandas as pd

# 定義你要抓取的股票代碼，這裡以蘋果公司 (AAPL) 為例
stock_symbol = '2330.tw'

# 設定日期範圍
start_date = '2023-01-01'
end_date = '2023-12-31'

# 使用 yfinance 抓取數據
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# 顯示數據
print(stock_data)