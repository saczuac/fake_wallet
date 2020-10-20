import os

import falcon

from .settings import STORAGE_PATH

from falcon_cors import CORS

from .store import Store

from .api.balances import Balances
from .api.transactions import Transactions

def create_app(store):
    cors = CORS(
                allow_all_headers=True,
                allow_all_methods=True,
                allow_credentials_all_origins=True,
                allow_all_origins=True
            )

    api = falcon.API(middleware=[cors.middleware])

    # Wallet Endpoints
    api.add_route('/api/transactions/{currency}/', Transactions(store))
    api.add_route('/api/balances/', Balances(store))
    return api


def get_app():
    storage_path = os.environ.get('LOOK_STORAGE_PATH', STORAGE_PATH)
    store = Store(storage_path)
    return create_app(store)
