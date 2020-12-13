from collections import Counter

TEST1 = '''R8,U5,L5,D3
U7,R6,D4,L4'''

TEST2 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''

TEST3 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''


direction = {
    'U': (0 , 1),
    'D': (0 ,-1),
    'L': (-1, 0),
    'R': (1 , 0),
}

def getPathSet(inp: str) -> set:
    c = (0, 0)
    p = set()
    for inst in inp.split(','):
        for _ in range(int(inst[1:])):
            d = direction[inst[0].upper()]
            c = d[0] + c[0], d[1] + c[1]
            p.add(c)
    return p

def getSetIntersections(inp: str) -> set:
    sets = [getPathSet(x) for x in inp.splitlines()]
    return sets[0].intersection(sets[1])

def getClosestIntersect(inp: set) -> tuple:
    return min(inp, key=lambda x: abs(x[0]) + abs(x[1]))

def findManhattenDist(x: int, y: int, p: tuple) -> int:
    return abs(x - p[0]) + abs(y - p[1])

assert getClosestIntersect(getSetIntersections(TEST1)) == (3, 3)
assert getClosestIntersect(getSetIntersections(TEST2)) == (155, 4)
assert getClosestIntersect(getSetIntersections(TEST3)) == (124, 11)
assert findManhattenDist(0,0,getClosestIntersect(getSetIntersections(TEST2))) == 159

with open('./inputs/day03.txt') as f:
    p1 = f.read()

wire_intersects = getSetIntersections(p1)
closest_intersect = getClosestIntersect(wire_intersects)

print('Part1: shortest path Manhatten style:')
print(closest_intersect, findManhattenDist(0, 0, closest_intersect))

# Part 2:
TEST4 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'

def traceIntersects(path: str, intersects: set) -> list:
    c = (0, 0)
    step = 0
    out = []
    for inst in path.split(','):
        for _ in range(int(inst[1:])):
            d = direction[inst[0].upper()]
            c = d[0] + c[0], d[1] + c[1]
            step += 1
            if c in intersects:
                out.append( (step, c) )
    return out

cnt = Counter()
t_ints = getSetIntersections(p1)
for wire in p1.split('\n'):
    for x in traceIntersects(wire, t_ints):
        cnt[(x[1])]+=x[0]

print(f'Part2: shortest path along wires:\n{cnt.most_common()[-1]}')