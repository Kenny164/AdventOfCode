from typing import List, Tuple, NamedTuple

def getInput() -> List[str]:
    with open("./inputs/day8.txt", "r") as f:
        out = list(map(int, f.readline().split()))
    return out

class Node:
    _metaSum = 0
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
    
    def getMetaSum(self):
        metaSum = 0
        for c in self.children:
            metaSum += sum(c.meta) + c.getMetaSum()
        if self.level == 0:
            return metaSum + sum(self.meta)
        return metaSum

    def __str__(self):
        return str("NODE: %dx Children and %dx metadata" % (self.childCount,self.metaCount))
        
def starOne(inputList: List[str]) -> str:
    root = Node(inputList)
    print(root.getMetaSum())
    print(root._metaSum)

def starTwo() -> int:
    pass

if __name__ == "__main__":
    inputList = getInput()
    #print(inputList)
    starOneOut = starOne(inputList)
    # print(starOneOut)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)