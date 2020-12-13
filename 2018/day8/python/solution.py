from typing import List, Tuple, NamedTuple

def getInput() -> List[str]:
    with open("./inputs/day8.txt", "r") as f:
        out = list(map(int, f.readline().split()))
    return out

class Node:
    def __init__(self, inputList: List[str], level: int = 0):
        self.childCount = inputList.pop(0)
        self.metaCount = inputList.pop(0)
        self.level = level
        self.children = []
        self.meta = []

        for i in range(self.childCount):
            self.children.append(Node(inputList, level+1))
        
        for i in range(self.metaCount):
            meta = inputList.pop(0)
            self.meta.append(meta)
    
    def getP1(self):
        metaSum = sum(self.meta)
        for c in self.children:
            metaSum += c.getP1()
        return metaSum
        
    def getP2(self):
        if len(self.children) == 0:
            return sum(self.meta)
        s = 0
        for c in self.meta:
            if len(self.children) >= c:
                s += self.children[c-1].getP2()
        return s

    def __str__(self):
        return str("NODE: %dx Children and %dx metadata" % (self.childCount,self.metaCount))

if __name__ == "__main__":
    rootNode = Node(getInput())
    print(rootNode.getP1())
    print(rootNode.getP2())