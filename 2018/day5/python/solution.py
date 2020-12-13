from typing import List, Tuple
from collections import Counter

def getInput():
    with open("./inputs/day5.txt","r") as f:
        return f.readlines()[0]

def reducePolymer(units: List[str]):
    stats = set()
    out = list()
    for u in units:
        stats.add(u.upper())
        if out and u.upper() == out[-1].upper() and u != out[-1]:
            out.pop()
        else:
            out.append(u)
    return out, stats

def removeStaticUnit(polymer: List[str], letter: str):
    out = list()
    for u in polymer:
        if u.upper() != letter.upper():
            out.append(u)
    return out

def starOne(polymer: List[str]):
    result = reducePolymer(polymer)
    return result

def starTwo(starOneResults: Tuple):
    stats = Counter()
    reducedPolymer, letterList = starOneResults
    for letter in letterList:
        improvedPolymer = removeStaticUnit(reducedPolymer, letter)
        result, _ = reducePolymer(improvedPolymer)
        stats[letter] = len(result)
    return result, stats.most_common()[-1]

if __name__ == "__main__":
    polymerStr = getInput()
    starOneOut = starOne(list(getInput()))
    print(len(starOneOut[0]))
    starTwoOut = starTwo(starOneOut)
    print(starTwoOut[1])
    # assert ''.join(starTwo(('dabAcCaCBAcCcaDA','a'))) == 'dbCBcD'
    # assert ''.join(starTwo(('dabAcCaCBAcCcaDA','b'))) == 'daCAcaDA'
    # assert ''.join(starTwo(('dabAcCaCBAcCcaDA','c'))) == 'daDA'
    # assert ''.join(starTwo(('dabAcCaCBAcCcaDA','d'))) == 'abCBAc'