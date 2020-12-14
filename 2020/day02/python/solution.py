import fileinput
import re
from collections import Counter

r_pattern = re.compile(r'^(?P<min>\d+)\-(?P<max>\d+)\s+(?P<letter>\w+):\s+(?P<str>\w+)$')
part1 = []
part2 = []
for line in fileinput.FileInput():
	groups = r_pattern.match(line)
	l_min, l_max, l_letter, l_str = groups.groups()
	ch_count = Counter()
	for char in l_str:
		ch_count.update(char)
	letter_count = ch_count[l_letter]
	if letter_count >= int(l_min) and letter_count <= int(l_max):
		part1.append(line)
	if (l_str[int(l_min)-1]==l_letter) ^ (l_str[int(l_max)-1]==l_letter):
		part2.append(line)


print(f'Part1: {len(part1)}')
print(f'Part2: {len(part2)}')