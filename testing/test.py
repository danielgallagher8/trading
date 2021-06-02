import sys

sys.path.append('../')


from datetime import datetime
from binance import main, database

b = main.Binance()


while __name__ == '__main__':
    d = database.Database()
    current_time = datetime.now()
    if current_time.strftime('%S') == '00':
        data_list = b.get_price()
        db = d.get_db()
        for data in data_list: 
            query = "INSERT INTO market_data (time, symbol, price) VALUES ('{}', '{}', '{}')".format(current_time.strftime('%H:%M'), data['symbol'], data['price'])
            db.execute(query)
            db.commit()
        db.close()
        print('Uploaded: {}'.format(current_time))
