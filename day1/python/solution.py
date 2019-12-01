def starOne():
    rollingTotal = 0
    for line in open("./inputs/day1.txt","r"):
        rollingTotal += int(int(line) / 3) - 2 
    return rollingTotal

def calcFuelRec(mass, roll):
    fuel = int(int(mass) / 3) - 2
    if fuel < 1:
        return 0
    return calcFuel(fuel, roll)

def calcFuel(mass):
    rollingTotal = 0
    fuel = mass
    while True:
        fuel = int(fuel / 3) - 2
        if fuel > 0: 
            rollingTotal += fuel
        else:
            break
    return rollingTotal

assert calcFuel(14) == 2
assert calcFuel(1969) == 966

def starTwo():
    rollingTotal = 0
    for line in open("./inputs/day1.txt","r"):
        #rollingTotal += calcFuelRec(int(line), 0)
        rollingTotal += calcFuel(int(line))
    return rollingTotal

if __name__ == "__main__":
    print(starTwo())
    pass