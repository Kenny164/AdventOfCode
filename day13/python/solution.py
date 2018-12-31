from typing import List, Tuple, NamedTuple
from enum import Enum

def getInput() -> List[str]:
    with open("./inputs/day13Test.txt", "r") as f:
        out = list(map(int, f.readline().split()))
    return out

Direction = Enum('Direction', ['UP','DOWN','LEFT','RIGHT'])
Turn = Enum('Turn', ['LEFT','RIGHT','STRAIGHT'])

class Track:
    def __init__(self, input: List[str], level: int = 0):
        self.childCount = input.pop(0)
        self.metaCount = input.pop(0)
        self.level = level
        self.children = []
        self.meta = []

        for i in range(self.childCount):
            self.children.append(Node(input, level+1))
        
        for i in range(self.metaCount):
            meta = input.pop(0)
            type(self)._metaSum += meta
            self.meta.append(meta)
        
def starOne():
    pass

def starTwo() -> int:
    pass

if __name__ == "__main__":
    pass
    # inputList = getInput()
    # #print(inputList)
    # starOneOut = starOne(inputList)
    # print(starOneOut)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)