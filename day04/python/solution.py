from collections import Counter

def hasMulti(inp: str, n: int = 0) -> bool:
    return len([x for x in zip(inp, inp[1:]) if x[0] == x[1]]) > n

def isAscending(inp: str) -> bool:
    return sorted(inp) == list(inp)

def hasPairs(inp: str) -> bool:
    return 2 in Counter(inp).values()

assert hasMulti('11233') == True
assert hasMulti('12323') == False
assert hasPairs('123444') == False
assert isAscending('11233') == True
assert isAscending('12323') == False

p1 = [x for x in range(367479, 893698) if hasMulti(str(x)) and isAscending(str(x))]
p2 = [x for x in range(367479, 893698) if hasPairs(str(x)) and isAscending(str(x))]

print(len(p1))
print(len(p2))