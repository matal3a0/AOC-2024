#!/usr/bin/env python

import sys

def check(r):
    inc = False
    dec = False 
    for i in range(len(r)-1):
        safe = True
        diff = r[i]-r[i+1]
        if abs(diff) < 1 or abs(diff) > 3 or diff == 0:
            safe = False
            break
        if diff < 0:
            inc = True
        elif diff > 0:
            dec = True
    if inc and dec:
        safe = False

    return safe


def main():
    data = [ list(map(int, line.strip().split())) for line in sys.stdin.readlines() ]
    
    reports1 = 0
    reports2 = 0

    for d in data:
        if check(d):
            reports1 += 1
    
    for d in data:
        if check(d):
            reports2 += 1
        else:
            for i in range(len(d)):
                c = d.copy()
                del c[i]
                if check(c):
                    reports2 += 1
                    break

    print("Part 1:", reports1)
    print("Part 2:", reports2)

if __name__ == "__main__":
    main()
