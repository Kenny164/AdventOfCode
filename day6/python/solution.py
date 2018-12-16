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

def closestPointFromList(x: int, y: int, points: List[Point]) -> Point:
    distances: List[Tuple[Point, int]] = []
    for p in points:
        distances.append( (p, findManhattenDist(x, y, p)) )
    distances.sort(key=lambda dist: dist[1])
    if distances[0][1] < distances[1][1]:
        return distances[0][0]
    return 0

def getCanvasSize(knownCoords: List[Point]) -> Tuple[int, int]:
    maxX = max(v[0] for v in knownCoords)
    maxY = max(v[1] for v in knownCoords)
    return maxX, maxY

def totalDistanceUnderN(x: int, y: int, points: List[Point], n: int) -> bool:
    total: int = 0
    for p in points:
        total += findManhattenDist(x, y, p)
    return total < n

def starOne(knownCoords: List[Point]) -> Point:
    count = Counter()
    ignoredPoints = set()
    maxX, maxY = getCanvasSize(knownCoords)
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

def starTwo(knownCoords: List[Point]) -> int:
    count: int = 0
    maxX, maxY = getCanvasSize(knownCoords)
    for y in range(maxY):
        for x in range(maxX):
            if totalDistanceUnderN(x, y, knownCoords, 10000):
                count += 1
    return count

if __name__ == "__main__":
    knownCoords = getInput()
    starOneOut = starOne(knownCoords)
    print(starOneOut)
    starTwoOut = starTwo(knownCoords)
    print(starTwoOut)