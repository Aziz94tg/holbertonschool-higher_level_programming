#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    else:
        return result
