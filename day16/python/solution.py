import re
from typing import List, NamedTuple
from collections import defaultdict, Counter

Sample = NamedTuple('Sample', [('before', List[int]), ('instruction', List[int]), ('after', List[int])])

def getInput():
    with open("./inputs/day16.txt","r") as f:
        data = f.read()
    return data

part1_regex = r"Before:\s+\[(.*)\]\n(.+)\nAfter:\s+\[(.+)\]\n"
Samples: List[Sample] = []

for (before, instruction, after) in re.findall(part1_regex, getInput()):
    b = [int(x) for x in before.split(",")]
    i = [int(x) for x in instruction.split(" ")]
    a = [int(x) for x in after.split(",")]
    Samples.append(Sample(b,i,a))

#print(Samples)

operation_fn = {
    'addr': lambda before, a, b: before[a] + before[b],
    'addi': lambda before, a, b: before[a] + b,
    'mulr': lambda before, a, b: before[a] * before[b],
    'muli': lambda before, a, b: before[a] * b,
    'banr': lambda before, a, b: before[a] & before[b],
    'bani': lambda before, a, b: before[a] & b,
    'borr': lambda before, a, b: before[a] | before[b],
    'bori': lambda before, a, b: before[a] | b,
    'setr': lambda before, a, b: before[a],
    'seti': lambda before, a, b: a,
    'gtir': lambda before, a, b: 1 if a > before[b] else 0,
    'gtri': lambda before, a, b: 1 if before[a] > b else 0,
    'gtrr': lambda before, a, b: 1 if before[a] > before[b] else 0,
    'eqir': lambda before, a, b: 1 if a == before[b] else 0,
    'eqri': lambda before, a, b: 1 if before[a] == b else 0,
    'eqrr': lambda before, a, b: 1 if before[a] == before[b] else 0,
}

SamplesWithMoreThan3Possible = 0

def exec_operation(before: List[int], instruction: List[int]):
    result = before[:]
    result[instruction[3]] = operation_fn[operation](before, instruction[1], instruction[2])
    return result

for s in Samples:
    PossibleCount = 0

    for operation in operation_fn:
        out = exec_operation(s.before, s.instruction)
        if out == s.after:
            PossibleCount += 1
        # print(f'{operation}:\t{s.before}\t{s.instruction}\t{actual}{s.after}\t{actual == s.after}')

    if PossibleCount >=3:
        SamplesWithMoreThan3Possible+=1
        #print(f'{operation}:\t{s.before}\t{s.instruction}\t{actual}{s.after}\t{actual == s.after}')

    #break

print(f'Part 1:\t{SamplesWithMoreThan3Possible}')
#print(f'Part 2:\t{counter}')