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
    return totalCount[2] * totalCount[3]
        
def starTwo(input):
    totalCount = []
    minDiff = 100
    index1 = 0
    index2 = 0
    matching = []
    for i in range(len(input)):
        for j in range(len(input)):
            diffCount = 0
            for letter in range(len(input[j])):
                diffCount = diffCount + 1 if input[j][letter] != input[i][letter] else diffCount
            totalCount.append((diffCount,i,j))
    for i in totalCount:
        if i[0] == 1:
            minDiff=i[0]
            index1=i[1]
            index2=i[2]
    #print("minDiff: %d\nindex1: %d\nindex2: %d" % (minDiff,index1,index2,))
    for i in range(len(input[index1])):
        if input[index1][i] == input[index1][i]:
            matching.append(input[index1][i])
    return ''.join(matching)

if __name__ == "__main__":
    input = getInput()
    print(starOne(input))
    print(starTwo(input))