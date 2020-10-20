STORAGE_PATH = './fake_wallet/db/'

try:
    from .local_settings import *
except ImportError:
    pass
