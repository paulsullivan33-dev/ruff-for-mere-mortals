import json


def load_config(path):
    with open(path) as handle:
        return json.load(handle)
