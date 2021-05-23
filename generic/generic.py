"""
Generic definitions / classes to be used throughout app
"""

#Import libraries
import json

def load_json(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data
