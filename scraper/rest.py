import requests


def _req(url, params=None, stream=False):
    res = requests.get(url, params, stream=stream)
    if not res.ok:
        raise Exception('status code was {}'.format(res.status_code))
    return res


def get_json(url, params=None):
    res = _req(url, params)
    return res.json()


def get_image(url, params=None):
    res = _req(url, params, stream=True)
    return res
