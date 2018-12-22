import re
from typing import List, Tuple, NamedTuple
from collections import Counter

Dependancy = NamedTuple('Dependancy', [('step', str), ('dependsOn', str)])

def getInput() -> List[Dependancy]:
    r_pattern = re.compile(r'^Step (?P<dependsOn>\w+) must be finished before step (?P<step>\w+) can begin\.$')
    out: List[Dependancy] = []
    allLetters = set()
    for line in open("./inputs/day7.txt", "r"):
        groups = r_pattern.match(line)
        out.append(Dependancy(groups['step'], groups['dependsOn']))
        allLetters.add(groups['step'])
        allLetters.add(groups['dependsOn'])
    return out, allLetters

def walkDependancies(deps: List[Dependancy], allLets: set) -> List[str]:
    out = []
    #unfinished = set(b for (a, b) in deps) - set(a for (a, b) in deps)
    while allLets:
        activeLetter = [l for l in sorted(allLets) if l not in [d.step for d in deps]][0]
        popDeps = [d for d in deps if d.dependsOn == activeLetter]
        print('running job %s free\'s up %s jobs' % (activeLetter, len(popDeps)))
        out.append(activeLetter)
        allLets.remove(activeLetter)
        for j in popDeps:
            deps.remove(j)
        #allLets.remove(nextJob)
    return out
        
def starOne(deps: List[Dependancy], allLets: set) -> str:
    result = walkDependancies(deps, allLets)
    return ''.join(result)

def starTwo(steps: List[Dependancy]) -> int:
    pass

if __name__ == "__main__":
    deps, allLets = getInput()
    starOneOut = starOne(deps, allLets)
    print(starOneOut)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)