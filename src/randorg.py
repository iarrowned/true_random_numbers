import requests
import json


class Randorg:

    def __init__(self):
        self.url = 'https://api.random.org/json-rpc/4/invoke'
        self.api_token = '69aa35db-90e1-4702-923f-1a285aa1778e'
        self.headers = {'content-type': 'application/json'}

    def req(self, mtd, n, min_, max_, replacement, base):
        json_str = {
            "jsonrpc": "2.0",
            "method": mtd,
            "params": {
                "apiKey": self.api_token,
                "n": n,
                "min": min_,
                "max": max_,
                "replacement": replacement,
                "base": base
            },
            "id": 42
        }
        return requests.post(self.url, json.dumps(json_str), headers=self.headers)

    def generateIntegers(self, n, min_=1, max_=100, replacement=True, base=10):
        res = self.req('generateIntegers', n, min_, max_, replacement, base).json()['result']['random']['data']
        if len(res) == 1:
            return res[0]
        else:
            return res
