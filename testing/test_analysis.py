import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


db = sqlite3.connect('binance_20210519.sqlite')
s = db.execute('SELECT * FROM market_data')

rows = []
for row in s:
    rows.append(row)

db.close()

df = pd.DataFrame(rows, columns=['time', 'symbol', 'price'])
df = df[df['symbol']=='BTCGBP']
df = df.astype({'time':'datetime64', 'price':'float'})
df = df.drop(['symbol'], axis=1)
df = df.set_index('time')

delta = df

for row in delta.iterrows():
    print(row)

#plt.plot([BTCGBP['time'], BTCGBP['price']])
#plt.show() #Doesn't work as data types are wrong 
