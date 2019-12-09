import os
import json
from os import path


def _ensure_dir(directory):
    if not path.isdir(directory):
        os.makedirs(directory)


def output_json(directory, filename, data):
    _ensure_dir(directory)
    with open('{}/{}'.format(directory, filename), mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent='  ')


def output_chunked_file(directory, filename, data):
    _ensure_dir(directory)
    with open('{}/{}'.format(directory, filename), mode='wb') as f:
        for chunk in data:
            f.write(chunk)
