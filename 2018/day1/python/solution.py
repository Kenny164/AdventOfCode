def starOne():
    rollingTotal = 0
    for line in open("./inputs/day1.txt","r"):
        rollingTotal += int(line)
    return rollingTotal

def starTwo():
    rollingTotal = 0
    historicTotal = set({rollingTotal})
    with open("./inputs/day1.txt","r") as f:
        extractedInts = map(int,f)
        for _ in range(100000000):
            for i in extractedInts:
                rollingTotal += i
                if rollingTotal in historicTotal:
                    return rollingTotal 
                historicTotal.add(rollingTotal)

if __name__ == "__main__":
    print(starTwo())