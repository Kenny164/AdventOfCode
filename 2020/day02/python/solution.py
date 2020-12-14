import fileinput
import re
from collections import Counter

r_pattern = re.compile(r'^(?P<min>\d+)\-(?P<max>\d+)\s+(?P<letter>\w+):\s+(?P<str>\w+)$')
part1 = []
part2 = []
for line in fileinput.FileInput():
	ch_count = Counter()
	groups = r_pattern.match(line)
	matched = groups.groupdict()
	for char in matched['str']:
		ch_count.update(char)
	letter_count = ch_count[matched['letter']]
	if letter_count >= int(matched['min']) and letter_count <= int(matched['max']):
		part1.append(matched)


print(f'Part1: {len(part1)}')
print(f'Part2: {len(part2)}')