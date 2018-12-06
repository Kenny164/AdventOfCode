from collections import Counter

def getInput():
    out = []
    for line in open("./inputs/day2.txt","r"):
        out.append(line.strip())
    return out

def starOne(input):
    totalCount = Counter()
    for line in input:
        c = Counter(line)
        CountSet = set(c.values())
        totalCount.update(CountSet)
        #print(CountSet[2])
    return totalCount[2] * totalCount[3]
        
def starTwo():
    pass

if __name__ == "__main__":
    input = getInput()
    print(starOne(input))