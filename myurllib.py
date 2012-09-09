"""Urllib with throttling to prevent myself from doing anything stupid again.
"""

import urllib
import time

_requests = {}
def urlopen(path):
    currtime = time.time()
    if path in _requests and (currtime - _requests[path]) < 30:
        raise ValueError("PATH: '{}'\nwas already recently "
                "requested!!!".format(path))
    print "urllib(mine) sleeping to throttle requests"
    time.sleep(0.25)
    return urllib.urlopen(path)

