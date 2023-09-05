#! /usr/bin/python3

import sys

code: int = int(sys.argv[1])

if (code == 0):
    print("\033[96m{}\033[0m".format("OK. 0"))
elif (code == 127):
    print("\033[95m{}\033[0m".format("UNKNWN. 127"))
else:
    print("\033[91m{}\033[0m".format(f'ERR. {code}'))

