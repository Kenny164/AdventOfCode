def starOne():
    rollingTotal = 0
    for line in open("./inputs/day1.txt","r"):
        rollingTotal += int(line)
    return rollingTotal

def starTwo():
    pass

if __name__ == "__main__":
    print(starOne())