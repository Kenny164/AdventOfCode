rollingTotal = 0
for line in open("./inputs/day1.txt","r"):
    rollingTotal += int(line)
print(rollingTotal)