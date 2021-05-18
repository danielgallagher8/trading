"""
Main Binance script
"""

#Import libraries
import requests
import re
import json
from urllib.parse import urlencode
#import time
#import datetime

#Define classes

base_endpoint = "https://api.binance.com"
alt_endpoints = ["https://api1.binance.com", "https://api2.binance.com", "https://api3.binance.com"]

class Binance:
    
    def __init__(self, *args, **kwargs):
        #self.api_key = self.get_json()['api_key']
        #self.secret_key = self.get_json()['secret_key']
        self.base_url = self.get_base_endpoint() + '/api/v3'
    
    def get_base_endpoint(self):
        if self.ping(base_endpoint).status_code == 200:
            return base_endpoint  
        else:
            for url in alt_endpoints:
                if self.ping(url).status_code == 200:
                    return url
    
    def ping(self, url):
        url = url + '/api/v3/ping'
        return requests.get(url)
    
    def http_code(self, code):
        if code == 403:
            return "WAF Limit (Web Application Firewall) has been violated"
        elif code == 429:
            return "breaking a request rate limit"
        elif code == 418:
            return "IP has been auto-banned for continuing to send requests after receiving 429 codes"
        elif re.search('^4', str(code)):
            return "malformed request"
        elif re.search('^5', str(code)):
            return " internal error"
    
    def pause_app(self):
        """
        If max weight has been used pause app for specified time
        """
        pass
    
    def get_json(self):
        with open('config.json') as config:
            data = json.load(config)
        return data
    
    def _params(self, params):
        rem_keys = []
        for key, val in params.items():
            if val is None:
                rem_keys.append(key)
        for key in rem_keys:
            del params[key]
        return params
    
    def _get(self, path, params=None):
        url = self.base_url + path
        if params != None:
            params = self._params(params)
            query = urlencode(params)
            url = f"{url}?{query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return self.http_code(response.status_code)
    
    def _post(self, path, params=None):
        url = self.base_url + path
        return url
    
    def get_server_time(self):
        return self._get('/time')
    
    def get_exchange_info(self, symbol=None):
        params = {'symbol':symbol}
        return self._get('/exchangeInfo', params)
    
    def get_depth(self, symbol, limit=None):
        params = {'symbol':symbol, 'limit':limit}
        return self._get('/depth', params)
    
    def get_recent_trades(self, symbol, limit=None):
        params = {'symbol':symbol, 'limit':limit}
        return self._get('/trades', params)
    
    def get_old_trades(self, symbol, limit=None, fromId=None):
        params = {'symbol':symbol, 'limit':limit, 'fromId':fromId}
        return self._get('/historicalTrades', params)
    
    def get_agg_trades(self, symbol, limit=None, fromId=None, startTime=None, endTime=None):
        params = {'symbol':symbol, 'limit':limit, 'fromId':fromId, 'startTime':startTime, 'endTime':endTime}
        return self.get('/aggTrades', params)
    
    def get_kline_data(self, symbol, interval, startTime=None, endTime=None, limit=None):
        params = {'symbol':symbol, 'interval':interval, 'startTime':startTime, 'endTime':endTime, 'limit':limit}
        return self._get('/klines', params)
    
    def get_avg_price(self, symbol):
        params = {'symbol':symbol}
        return self._get('/avgPrice', params)
    
    def get_daily_change(self, symbol):
        params = {'symbol':symbol}
        return self._get('/ticker/24hr', params)
    
    def get_price(self, symbol=None):
        params = {'symbol':symbol}
        return self._get('/ticker/price', params)
    
    def get_book_tickers(self, symbol):
        params = {'symbol':symbol}
        return self._get('/ticker/bookTicker', params)
    
    def post_order(self):
        pass
    
b = Binance()
    
            