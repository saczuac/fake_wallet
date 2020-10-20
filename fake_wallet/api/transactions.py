from random import random

import falcon

import json


FILENAME = 'transactions.json'


class Transactions(object):
    def __init__(self, store):
        self._store = store

    def on_get(self, req, resp, currency):
        with self._store.open(FILENAME) as f:
            data = json.load(f)['transactions']

        resp_data = [d for d in data if d['currency'] == currency]
        resp.body = json.dumps(resp_data[0], ensure_ascii=False)

        resp.status = falcon.HTTP_200
