#!/usr/bin/python3

import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3+")
import pip
help(pip)
print("Ready for test")