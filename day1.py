#!/usr/bin/env python

import sys

data = [line.strip() for line in sys.stdin.readlines()]

d1 = []
d2 = []

for d in data:
    x = d.split()
    d1.append(int(x[0]))
    d2.append(int(x[1]))

d1 = sorted(d1)
d2 = sorted(d2)

diff = 0
sim = 0

for i in range(len(d1)):
    diff += (abs(d1[i]-d2[i]))
    sim += d1[i]*d2.count(d1[i])

print("Part 1:", diff)
print("Part 2:", sim)

