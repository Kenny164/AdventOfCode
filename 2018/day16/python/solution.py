import re, random
from typing import List, NamedTuple, Iterator, Tuple
from collections import defaultdict, Counter

Sample = NamedTuple('Sample', [('before', List[int]), ('instruction', List[int]), ('after', List[int])])

def getInput():
    samples: List[Sample] = []
    program: List[List[int]] = []
    part1_regex = r"Before:\s+\[(.*)\]\n(.+)\nAfter:\s+\[(.+)\]\n?"
    with open("./inputs/day16.txt","r") as f:
        data = f.read().split('\n\n\n\n')
    for (before, instruction, after) in re.findall(part1_regex, data[0]):
        b = [int(x) for x in before.split(",")]
        i = [int(x) for x in instruction.split(" ")]
        a = [int(x) for x in after.split(",")]
        samples.append(Sample(b, i, a))
    for oper in data[1].strip().split('\n'):
        op, a, b, c = oper.split()
        program.append([op, a, b, c])
    return (samples, program)

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

def exec_operation(operation: str, before: List[int], instruction: List[int]) -> List[int]:
    result = before[:]
    result[instruction[3]] = operation_fn[operation](before, instruction[1], instruction[2])
    return result

def possible_ops(sample: Sample) -> Iterator[str]:
    for operation in operation_fn:
        out_f = exec_operation(operation, sample.before, sample.instruction)
        if out_f == s.after:
            yield operation

samples, program = getInput()

poss: List[Tuple[int, set]] = []
for s in samples:
    poss.append((s.instruction[0], set(p for p in possible_ops(s))))

print(f'Part 1:\t{ len([x for x in poss if len(x[1]) >= 3])} ')

edges = [set(operation_fn.keys()) for _ in operation_fn]
for i in poss:
    edges[i[0]] &= i[1] # inline intersection (removing the non-successful)

while len([i for i in edges if len(i) > 1]) > 0:
    for i, e in enumerate(edges):
        if len(e) == 1:
            for j, other in enumerate(edges):
                if j != i:
                    edges[j] -= e

opcode_lookup = [next(iter(x)) for x in edges]
regs = 4*[0]

for instruction in program:
    instruction = list(map(int, instruction))
    op = opcode_lookup[instruction[0]]
    regs = exec_operation(op, regs, instruction)


print(f'Part 2:\t{ regs }')