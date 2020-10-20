import falcon

import json

FILENAME = 'balances.json'


class Balances(object):
    def __init__(self, store):
        self._store = store

    def on_get(self, req, resp):
        with self._store.open(FILENAME) as f:
            data = json.load(f)

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200
