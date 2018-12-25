from typing import DefaultDict


def findPowerLevel(x: int, y: int, gridSerialId: int) -> int:
    rackId = x + 10
    init_power = rackId * y
    powerLevel = init_power + gridSerialId
    powerLevel *= rackId
    powerLevel = int(powerLevel // 100 % 10)
    powerLevel -= 5
    return powerLevel

assert findPowerLevel(3, 5, 8) == 4
assert findPowerLevel(122, 79, 57) == -5
assert findPowerLevel(217,196, 39) == 0
assert findPowerLevel(101,153, 71) == 4

# https://en.wikipedia.org/wiki/Summed-area_table
fuelCells = DefaultDict(int)
cellSums = DefaultDict(int)
cellTots = DefaultDict(int)
for y in range(1,300+1):
    for x in range(1,300+1):
        fuelCells[(x, y)] = findPowerLevel(x, y, 5719)
        cellSums[(x, y)] = fuelCells[x, y] + fuelCells[x - 1, y] + fuelCells[x, y - 1] - fuelCells[x - 1, y - 1]
        # Sum = D - B - C + A (D being current)
        cellTots[(x, y)] 

def starOne() -> int:
    pass

def starTwo() -> int:
    pass

if __name__ == "__main__":
    pass
    #starOneOut = starOne(5719)
    #print(starOneOut)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)