import sys
import re
from queue import PriorityQueue

with open("./inputs/day23.txt", "r") as f:
    bots = [list(map(int, re.findall('-?\d+', x))) for x in f.readlines() if len(x) > 0]

print(bots)