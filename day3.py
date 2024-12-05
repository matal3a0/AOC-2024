#!/usr/bin/env python

import re
import sys

data = sys.stdin.readline()
ops = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', data)
part1sum = 0
part2sum = 0
do = True

for o in ops:
    if o == 'do()':
        do = True
    elif o == "don't()":
        do = False
    else:
        a,b = re.findall(r'\d+',o)
        part1sum += int(a)*int(b)
        if do:
            part2sum += int(a)*int(b)

print("Part 1:",part1sum)
print("Part 2:",part2sum)

