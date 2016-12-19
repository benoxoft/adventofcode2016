#Find x*x + 3*x + 2*x*y + y + y*y.
#Add the office designer's favorite number (your puzzle input).
#Find the binary representation of that sum; count the number of bits that are 1.
#If the number of bits that are 1 is even, it's an open space.
#If the number of bits that are 1 is odd, it's a wall.

FAVOURITE_NUMBER = 1358
import numpy as np

MAP = {
    0: ".",
    1: "#",
    np.nan: ".",
    2: "@"
}


def process_location(x:int, y:int, fav_num:int) -> int:
    n = x*x + 3*x + 2*x*y + y + y*y
    n += fav_num
    b = bin(n)[2:]
    print(b, b.count("1"), b.count("1") % 2 == 0)
    #if x == 31 and y == 39:
    #    return 2
    if b.count("1") % 2 == 0:
        return 0
    else:
        return 1

np.set_printoptions(threshold=np.nan, linewidth=220, formatter={'all': lambda x: MAP[x]})

size = 300
floor = np.zeros((size, size))
print(floor)
#31,39
for x in range(0, size):
    for y in range(0, size):
        floor[y, x] = process_location(x, y, FAVOURITE_NUMBER)

print(floor)

graph = {}
for x in range(0, size-1):
    for y in range(0, size-1):
        graph[(x, y)] = []
        if x > 0 and floor[y, x-1] == 0:
            graph[(x, y)].append((x-1, y))
        if y > 0 and floor[y-1, x] == 0:
            graph[(x, y)].append((x, y-1))
        if x < size and floor[y, x+1] == 0:
            graph[(x, y)].append((x+1, y))
        if y < size and floor[y+1, x] == 0:
            graph[(x, y)].append((x, y+1))

import copy
def traverse_graph(x, y, graph, steps, locations):
    #print("Start", x, y)
    if (x, y) not in locations and len(steps) <= 50:
        locations.append((x, y))
        print(len(locations))
    if (x, y) in steps:
        return
    steps.append((x, y))
    for xx, yy in graph[x, y]:
        traverse_graph(xx, yy, graph, copy.copy(steps), locations)
        #if xx == 31 and yy == 39:
        #    if len(steps) < 100:
        #        minstep = len(steps)
        #        print(minstep)
        #    return


print("Starting")
print(graph[1,1])
traverse_graph(1, 1, graph, [], [])

#  0123456789
#0 .#.####.##
#1 ..#..#...#
#2 #....##...
#3 ###.#.###.
#4 .##..#..#.
#5 ..##....#.
#6 #...##.###
