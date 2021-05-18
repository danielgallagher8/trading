import sys

sys.path.append('../')


from datetime import datetime
from time import sleep
from binance import main as b

b = b.Binance()

while __name__ == '__main__':
    if datetime.now().strftime('%S') == '00':
        price = b.get_price()
        print(price)
        sleep(10)