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
    while allLets:
        activeLetter = [l for l in sorted(allLets) if l not in [d.step for d in deps]][0]
        popDeps = [d for d in deps if d.dependsOn == activeLetter]
        #print('running job %s free\'s up %s jobs' % (activeLetter, len(popDeps)))
        out.append(activeLetter)
        allLets.remove(activeLetter)
        for j in popDeps:
            deps.remove(j)
    return out

def walkDependanciesWithWorkers(deps: List[Dependancy], allLets: set, workerCount: int = 5) -> List[str]:
    out = []
    workers = [(None, 0)] * workerCount
    total_time = 0
    while allLets:
        total_time += 1
        # hand out jobs to available workers
        for i, w in enumerate(workers):
            if w == (None, 0):
                activeLetter = [l for l in sorted(allLets) if l not in [d.step for d in deps]]
                if activeLetter:
                    workers[i] = (activeLetter[0], 60+ord(activeLetter[0])-ord('A'))
                    allLets.remove(activeLetter[0])

        # finish up the tasks
        for i, w in enumerate(workers):
            if w == (None, 0): continue
            workers[i] = (w[0], w[1]-1)
            if w[1] == 0:
                popDeps = [d for d in deps if d.dependsOn == w[0]]
                for j in popDeps:
                    deps.remove(j)
                workers[i] = (None, 0)
    return max(w[1] for w in workers) + total_time + 1
        
def starOne(deps: List[Dependancy], allLets: set) -> str:
    result = walkDependancies(deps, allLets)
    return ''.join(result)

def starTwo(deps: List[Dependancy], allLets: set) -> str:
    return walkDependanciesWithWorkers(deps, allLets, 5)

if __name__ == "__main__":
    deps, allLets = getInput()
    starOneOut = starOne(deps, allLets)
    print(starOneOut)
    deps, allLets = getInput()
    starTwoOut = starTwo(deps, allLets)
    print(starTwoOut)