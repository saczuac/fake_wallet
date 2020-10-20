import io
import os
import re
import uuid
import mimetypes
import json

import falcon


class Store(object):

    def __init__(self, storage_path, fopen=io.open):
        self._storage_path = storage_path
        self._fopen = fopen

    def save(self, data, name):
        path = os.path.join(self._storage_path, name)

        with self._fopen(path, 'w') as file:
            json.dump(data, file)

        return name

    def open(self, name):

        path = os.path.join(self._storage_path, name)
        stream = self._fopen(path, 'rb')

        return stream