#!/usr/bin/python

class ImmutableDict(dict):
    def __delitem__(self, key):
        raise TypeError("objects are immutable")

    def __setitem__(self, key, value):
        raise TypeError("objects are immutable")

    def clear(self):
        raise TypeError("objects are immutable")

    def pop(self, key, default=None):
        raise TypeError("objects are immutable")

    popitem = clear

    def setdefault(self, key, value=None):
        raise TypeError("objects are immutable")

    def update(self, *args, **f):
        raise TypeError("objects are immutable")

    __setattr__ = update
    __delattr__ = update
