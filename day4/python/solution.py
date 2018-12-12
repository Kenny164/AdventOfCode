import re
from typing import NamedTuple, List
from collections import Counter

SleepLog = NamedTuple('SleepLog', [('guard', int), ('down', int), ('up', int)])

def getInput():
    records: List[str]
    with open("./inputs/day4.txt","r") as f:
        records = f.readlines()
    return sorted(records)

def CreateSleepLog(fromFile):
    r_pattern = re.compile(r'^\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)\s+(?P<hour>\d+):(?P<min>\d+)\]\s+(?P<log>.+)$')
    c_pattern = re.compile(r'Guard #(\d+) begins shift')
    sLog: List[SleepLog] = []
    temp: dict = {}
    for line in fromFile:
        lineMatch = r_pattern.search(line)
        logLine = lineMatch.group('log')
        isGuard = c_pattern.match(lineMatch.group('log'))
        if isGuard:
            temp['guard'] = int(isGuard.groups()[0])
        elif 'falls' in logLine:
            temp['down'] = int(lineMatch.group('min'))
        elif 'wakes' in logLine:
            temp['up'] = int(lineMatch.group('min'))
            sLog.append(SleepLog(temp['guard'], temp['down'], temp['up']))
    return sLog

def findSlacker(slog):
    sCount = Counter()
    for snooze in sLog:
        sCount[snooze.guard] += snooze.up - snooze.down
    return sCount.most_common(1)[0]

def getSlackerMins(sLog, slacker=None):
    minTracker = Counter()
    for guard in sLog:
        if slacker != None and guard.guard != slacker[0]:
            continue
        for x in range(guard.down, guard.up):
            minTracker[(guard.guard, x)] += 1
    (g, minute) = minTracker.most_common(1)[0][0]
    return g * minute

def starOne(sLog):
    worstGuard = findSlacker(sLog)
    return getSlackerMins(sLog, worstGuard)

def starTwo(sLog):
    return getSlackerMins(sLog)

if __name__ == "__main__":
    fromFile = getInput()
    sLog = CreateSleepLog(fromFile)
    print(starOne(sLog))
    print(starTwo(sLog))
    