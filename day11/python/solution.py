from typing import DefaultDict

def findPowerLevel(x: int, y: int, gridSerialId: int) -> int:
    rackId = x + 10
    init_power = rackId * y
    powerLevel = init_power + gridSerialId
    powerLevel *= rackId
    powerLevel = int(powerLevel // 100 % 10)
    powerLevel -= 5
    return powerLevel

# https://en.wikipedia.org/wiki/Summed-area_table
def getFuelCells(gridSerialId: int) -> tuple:
    fuelCells = DefaultDict(int)
    cellSums = DefaultDict(int)
    for y in range(1,300+1):
        for x in range(1,300+1):
            fuelCells[(x, y)] = findPowerLevel(x, y, gridSerialId)
            cellSums[(x, y)] = fuelCells[x, y] + cellSums[x - 1, y] + cellSums[x, y - 1] - cellSums[x - 1, y - 1]
    return fuelCells, cellSums

def getMaxSquare(cellSums, squareSize: int = 3) -> int:
    # Sum = D - B - C + A (D being current) will also need to offset since answer wants top-left
    cellTots = DefaultDict(int)
    for y in range(1,300+1):
        for x in range(1,300+1):
            A = cellSums[(x - squareSize, y - squareSize)]
            B = cellSums[(x, y - squareSize)]
            C = cellSums[(x - squareSize, y)]
            D = cellSums[(x, y)] 
            cellTots[(x-squareSize+1, y-squareSize+1)] = D - B - C + A
    maxOne = max(cellTots, key=lambda x: cellTots[x])
    return (maxOne, cellTots[maxOne])

def starOne(gridSerialId: int, squareSize: int) -> int:
    _, cellSums = getFuelCells(gridSerialId)
    out, _ = getMaxSquare(cellSums, squareSize)
    return out

def starTwo(gridSerialId: int) -> tuple:
    fuelCell, cellSums = getFuelCells(gridSerialId)
    maxList = []
    for size in range(1,32+1):
        maxIndex, maxValue = getMaxSquare(cellSums, size)
        maxList.append((maxIndex, maxValue, size))
    maxOne = max(maxList, key=lambda x: x[1])
    return maxOne

if __name__ == "__main__":
    assert findPowerLevel(3, 5, 8) == 4
    assert findPowerLevel(122, 79, 57) == -5
    assert findPowerLevel(217,196, 39) == 0
    assert findPowerLevel(101,153, 71) == 4
    starOneOut = starOne(5719, 3)
    print(starOneOut)
    assert starOne(18, 16) == (90,269)
    assert starOne(42, 12) == (232,251)
    starTwoOut = starTwo(5719)
    print(starTwoOut)