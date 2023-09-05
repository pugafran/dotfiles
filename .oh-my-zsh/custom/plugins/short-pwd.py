#! /usr/bin/python3

import os
from math import ceil

def get_max_length (directory_idx, directories) -> int:
    return min(len(directories[directory_idx]), ceil((directory_idx+1 / len(directories))*len(directories[directory_idx]))+1)

cwd: str = os.getcwd()
home: str = os.path.expanduser('~')
out: list[str] = []
if (cwd.find(home) == 0):
    out.append('~')
    cwd: str = cwd[len(home):]

directories: list[str] = list(filter(lambda x: x.strip() != "", cwd.split('/')))
for index, directory in enumerate(directories):
    out.append(
          directory[:get_max_length(index, directories)]
    )

for x in out[:len(out)-1]:
    print(x, end="/")
print(out[len(out)-1])

