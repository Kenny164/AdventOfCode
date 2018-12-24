from typing import List, Tuple, NamedTuple
import re

#Position = NamedTuple('Position', [('x', int), ('y', int), ('vx', int), ('vy', int)])
class Position:
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def __repr__(self):
        return f'pos:{self.x},{self.y} vol:{self.vx},{self.vy}'
    

def getInput() -> List[Position]:
    r_pattern = re.compile(r'^position=<\s?(?P<x>[-\d]+)\,\s*(?P<y>[-\d]+)> velocity=<\s?(?P<vx>[-\d]+)\,\s*(?P<vy>[-\d]+)>$')
    out = []
    for line in open("./inputs/day10.txt", "r"):
        x, y, vx, vy = map(int, r_pattern.match(line).groups())
        out.append(Position(x, y, vx, vy))
    return out

def tick(posList: List[Position], reverse: bool=False) -> None:
    if reverse:
        for p in posList:
            p.x += -p.vx
            p.y += -p.vy
        return
    for p in posList:
        p.x += p.vx
        p.y += p.vy

def bBoxSize(posList: List[Position]) -> Tuple[int, int]:
    minX = min([p.x for p in posList])
    minY = min([p.y for p in posList])
    maxX = max([p.x for p in posList])
    maxY = max([p.y for p in posList])
    bBox = (maxX - minX, maxY - minY)
    return bBox

def display(inputList) -> None:
    maxX, maxY = bBoxSize(inputList)
    offsetX = min([p.x for p in inputList])
    offsetY = min([p.y for p in inputList])
    positions = set([(p.x, p.y) for p in inputList])
    for y in range(offsetY+maxY+1):
        for x in range(offsetX+maxX+1):
            if (x, y) in positions:
                print('#', end='')
            else:
                print(' ', end='')
        print()
        
def starOne(inputList: List[Position]) -> int:
    bBox = bBoxSize(inputList)
    for i in range(20000):
        print(f'step {i}: {bBox}')
        tick(inputList)
        if bBox[1] < bBoxSize(inputList)[1]:
            tick(inputList, reverse=True)
            return i
        bBox = bBoxSize(inputList)
    raise 'bounding box size doesn\'t turn :('

def starTwo() -> int:
    pass

if __name__ == "__main__":
    inputList = getInput()
    #tick(inputList)
    starOneOut = starOne(inputList)
    print(starOneOut)
    display(inputList)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)