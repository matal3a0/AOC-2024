#!/usr/bin/env python

import sys

def main():
    data = [[l for l in line.strip()] for line in sys.stdin.readlines() ]

    part1sum = 0
    part2sum = 0

    height = len(data)
    width = len(data[0])

    for y in range(height):
        for x in range(width):
            if data[y][x] == 'X':
                # Left
                if x > 2 and data[y][x] + data[y][x-1] + data[y][x-2] + data[y][x-3] == 'XMAS':
                    part1sum += 1
                # Right
                if x < width-3 and data[y][x] + data[y][x+1] + data[y][x+2] + data[y][x+3] == 'XMAS':
                    part1sum += 1
                # Up
                if y > 2 and data[y][x] + data[y-1][x] + data[y-2][x] + data[y-3][x] == 'XMAS':
                    part1sum += 1
                # Down
                if y < height-3 and data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x] == 'XMAS':
                    part1sum += 1
                # Left up
                if x > 2 and y > 2 and data[y][x] + data[y-1][x-1] + data[y-2][x-2] + data[y-3][x-3] == 'XMAS':
                    part1sum += 1
                # Left down
                if x > 2 and y < height-3 and data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3] == 'XMAS':
                    part1sum += 1
                # Right up
                if x < width-3 and y > 2 and data[y][x] + data[y-1][x+1] + data[y-2][x+2] + data[y-3][x+3] == 'XMAS':
                    part1sum += 1
                # Right down
                if x < width-3 and y < height-3 and data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3] == 'XMAS':
                    part1sum += 1
    
            elif data[y][x] == 'A':
                if x > 0 and x < width-1 and y > 0 and y < height-1:
                    w1 = data[y-1][x-1] + data[y][x] + data[y+1][x+1] 
                    w2 = data[y+1][x-1] + data[y][x] + data[y-1][x+1]
                    if (w1 == 'MAS' and w2 == 'MAS') \
                        or (w1 == 'SAM' and w2 == 'SAM') \
                        or (w1 == 'SAM' and w2 == 'MAS') \
                        or (w1 == 'MAS' and w2 == 'SAM'):
                        part2sum += 1

    print("Part 1:", part1sum)
    print("Part 2:", part2sum)

if __name__ == "__main__":
    main()
