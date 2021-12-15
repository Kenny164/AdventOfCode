from typing import List

TEST="""199
200
208
210
200
207
240
269
260
263"""

def count_depths_inc(d: List[int], gap: int = 1) -> int:
    count = 0
    for i in range(len(d) - gap):
        if d[i] < d[i+gap]:
            count+=1
    return count

test_depths = [int(x) for x in TEST.split('\n')]
assert count_depths_inc(test_depths) == 7
assert count_depths_inc(test_depths, 3) == 5

if __name__ == "__main__":
    with open('./2021/inputs/day01.txt') as f:
        depths = [int(x) for x in f.read().split('\n')]
    print(f'Part1: {count_depths_inc(depths)}')
    print(f'Part2: {count_depths_inc(depths, 3)}')