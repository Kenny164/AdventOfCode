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

def getClosestIntersect(inp: str) -> tuple:
    sets = [getPathSet(x) for x in inp.splitlines()]
    intersects = sets[0].intersection(sets[1])
    return min(intersects, key=lambda x: abs(x[0]) + abs(x[1]))

def findManhattenDist(x: int, y: int, p: tuple) -> int:
    return abs(x - p[0]) + abs(y - p[1])

assert getClosestIntersect(TEST1) == (3, 3)
assert getClosestIntersect(TEST2) == (155, 4)
assert getClosestIntersect(TEST3) == (124, 11)
assert findManhattenDist(0,0,getClosestIntersect(TEST2)) == 159

with open('./inputs/day03.txt') as f:
    p1 = getClosestIntersect(f.read())

print(p1, findManhattenDist(0, 0, p1))

