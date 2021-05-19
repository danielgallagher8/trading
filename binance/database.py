"""
Database for Binance API 
"""

#Import libraries
import sqlite3
from datetime import datetime
import os

#Define classes
class Database:
    
    def __init__(self, *args, **kwargs):
        self.db_check()
        self.check_table()
        
    def today(self):
        return datetime.now().strftime('%Y%m%d')
    
    def current_time(self):
        return datetime.now().strftime('%H:%M')
    
    @property
    def db_name(self):
        return 'binance_{}.sqlite'.format(self.today())
    
    def db_check(self):
        if not os.path.exists(self.db_name):
            conn = sqlite3.connect(self.db_name)
            conn.close()
    
    def get_db(self):
        return sqlite3.connect(self.db_name)
    
    def check_table(self):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='market_data'"
        db = self.get_db()
        cursor = db.execute(query)
        rows = []
        for row in cursor:
            rows.append(row)
        if len(rows) > 0:
            exists = True
        else:
            exists = False
        if exists is False:
            query = "CREATE TABLE market_data (time nvarchar(50), symbol nvarchar(50), price nvarchar(50))"
            db.execute(query)
            db.commit()
            db.close()
            
    def db_close(self):
        conn = sqlite3.connect(self.db_name())
        conn.close()