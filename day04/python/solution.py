def hasMulti(inp: str) -> bool:
    return len([x for x in zip(inp, inp[1:]) if x[0] == x[1]]) > 0

def isAscending(inp: str) -> bool:
    return sorted(inp) == list(inp)

assert hasMulti('11233') == True
assert hasMulti('12323') == False
assert isAscending('11233') == True
assert isAscending('12323') == False

p1 = [x for x in range(367479, 893698) if hasMulti(str(x)) and isAscending(str(x))]

print(len(p1))