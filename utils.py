import pickle
import functools
from random import random

PICKLE_FILENAME = "data.pkl"

def make_writer(filename):
    try:
        data = pickle.load(open(filename, 'rb'))
    except:
        data = {}
    def writer(key, value):
        data[key] = value
        pickle.dump(data, open(filename, 'wb'))
    return writer

def write(f):
    def wf(writer):
        result = f()
        writer(f.__name__, result)
        #print result
    return wf

def get_cached(key, func):
    try:
        data = pickle.load(open(PICKLE_FILENAME))
        return data[key]
    except:
        return func()
