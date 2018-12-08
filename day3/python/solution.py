import re
import collections

def getInput():
    r_pattern = re.compile(r'^#(?P<id>\d+)\s+@\s+(?P<x>\d+)\,(?P<y>\d+):\s+(?P<width>\d+)x(?P<height>\d+)$')
    out = []
    for line in open("./inputs/day3.txt","r"):
        groups = r_pattern.match(line)
        out.append(groups.groupdict())
    return out

def displayFabric(fabric):
    print('\n'.join([''.join(['{}'.format(item) for item in row]) for row in fabric]))

def starOne(input):
    maxWidth =  max([int(x['x']) for x in input]) + max([int(x['width']) for x in input])
    maxHeight =  max([int(x['y']) for x in input]) + max([int(x['height']) for x in input])
    fabric = [x[:] for x in [[0] * maxWidth] * maxHeight]
    overlapCount = 0
    for claim in input:
        offset = (int(claim['x']), int(claim['y']))
        for y in range(offset[1], (offset[1] + int(claim['height']))):
            for x in range(offset[0], (offset[0] + int(claim['width']))):
                if fabric[y][x] != 0:
                    fabric[y][x] = 'X'
                    overlapCount += 1
                else:
                    fabric[y][x] = int(claim['id'])
    displayFabric(fabric)
    xCount = collections.Counter([x for row in fabric for x in row])['X']
    return xCount
        
def starTwo(input):
    pass

if __name__ == "__main__":
    input = getInput()
    print(starOne(input))
    print(starTwo(input))