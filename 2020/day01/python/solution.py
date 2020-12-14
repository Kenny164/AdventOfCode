import fileinput
GOAL = 2020

n = [int(x) for x in fileinput.input()]

for x in range(len(n)):
	for y in range(x, len(n)):
		if n[x] + n[y] == GOAL:
			print(f'part1: {n[x] * n[y]}')
		for z in range(y, len(n)):
			if n[x] + n[y] + n[z] == GOAL:
				print(f'part2: {n[x] * n[y] * n[z]}')