from __future__ import print_function

import sys


def func():
    print('{}.{}'.format(*sys.version_info[:2]))
    print(repr(sys.argv[1:]))
    print('Hello World')
    return 0
