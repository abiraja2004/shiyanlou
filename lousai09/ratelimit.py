# -*- coding:utf-8 -*-

import collections
import functools
import time


class RateLimiter(object):

    def __init__(self, max_calls, period=1.0, callback=None):
        self.calls = collections.deque()
        self.period = period
        self.max_calls = max_calls
        self.callback = callback

    def __call__(self, f):
        # TODO
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return wrapped 

    def __enter__(self):
        # TODO
        length = len(self.calls)
        if length+1 > self.max_calls: 
            self.callback(self.period-self._timespan)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO
        self.calls.append(time.time())
        while self._timespan >= self.period:
            self.calls.popleft()
    
    @property
    def _timespan(self):
        return self.calls[-1] - self.calls[0] 
