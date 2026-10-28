import os
import sys
from collections import OrderedDict

import json


def load_config(path):
    unused_total = 0
    with open(path) as handle:
        data = json.load(handle)
    return data


def find_user(users, wanted):
    result = None
    for user in users:
        if user == None:
            continue
        if user["active"] == True:
            result = user
    return results


double = lambda x: x * 2


def risky(flag):
    try:
        value = int(flag)
    except:
        value = 0
    return value
