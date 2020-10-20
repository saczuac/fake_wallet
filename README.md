# Fake Wallet
_Mock service for a Basic Wallet API_

## Setup
`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r requirements.txt`

Add every port you want to consume the API into the CORS whitelist in your local_settings, like this: 

```
CORS_WHITELIST = [
    'http://localhost:8080',
    'http://localhost:8001',
    'http://localhost:8002',
    'http://localhost:8003'
]
```

Run it:

`$ gunicorn --reload 'fake_wallet.app:get_app()' -w 2 -b :[PORT] -k 'eventlet'`

PORT = where the service is going to run. Example: 8000


## Supported endpoints

## WALLET

### `'/api/transactions/{currency}/'`
Methods: GET

### `'/api/balances/'`
Methods: GET
