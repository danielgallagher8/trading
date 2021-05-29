"""
Generic definitions / classes to be used throughout app
"""

#Import libraries

import json
from datetime import datetime
import jira_auto as j
import sys
from io import StringIO

#Define classes/defs

def load_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data

class Logging:
    
    def __init__(self, *args, **kwargs):
        self.current_date = datetime.now().strftime('%y%m%d')
        self.file()
    
    def file(self):
        open('logfile_{}'.format(self.current_date), 'a+')
    
    def log(self, error, file):
        current_time = datetime.now().strftime('%H:%M:%S')
        with open('logfile_{}'.format(self.current_date), 'a+') as f:
            f.write('{} | {} | {}'.format(current_time, file, error))
            f.close()
 
       
class Error:
    
    def __init__(self, *args, **kwargs):
        self.error = []
        self.run()
    
    def run(self):
        self.std_out = sys.stdout
        sys.stdout = self.string_io = StringIO()
        return self
    
    def output(self):
        self.error.extend(self.string_io.getvalue())
        del self.string_io
        sys.stdout = self.std_out
        print(self.error)
    
    def raise_jira(self, issue):
        j.Jira.create_issue(desc=issue)


e = Error()
print('hello')
e.output()