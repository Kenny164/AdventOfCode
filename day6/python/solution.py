from typing import List, Tuple, NamedTuple
from collections import Counter

Point = NamedTuple('Point', [('x', int), ('y', int)])

def getInput() -> List[Point]:
    knownCoords: List[Point] = []
    for line in open("./inputs/day6.txt", "r"):
        x, y = [int(p) for p in line.split(',')]
        knownCoords.append(Point(x, y))
    return knownCoords

def findManhattenDist(x: int, y: int, p: Point) -> int:
    return abs(x - p.x) + abs(y - p.y)

def closestPointFromList(x: int, y: int, points: List[Point]):
    distances: List[Tuple] = []
    for p in points:
        distances.append( (p, findManhattenDist(x, y, p)) )
    distances.sort(key=lambda dist: dist[1])
    if distances[0][1] < distances[1][1]:
        return distances[0][0]
    return 0

def starOne(knownCoords: List[Point]) -> Point:
    count = Counter()
    ignoredPoints = set()
    maxX = max(v[0] for v in knownCoords)
    maxY = max(v[1] for v in knownCoords)
    for y in range(maxY):
        for x in range(maxX):
            out = closestPointFromList(x,y,knownCoords)
            count[out] += 1
            if x == maxX or y == maxY or x == 0 or y == 0:
                ignoredPoints.add(out)
    for x in count:
        if x in ignoredPoints:
            count[x] = 0
    return count.most_common(1)[0]

if __name__ == "__main__":
    knownCoords = getInput()
    starOneOut = starOne(knownCoords)
    print(starOneOut)