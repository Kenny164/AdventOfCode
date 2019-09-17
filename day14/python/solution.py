from typing import List, Tuple, NamedTuple

class Scoreboard:
    def __init__(self, scores: List[int], elves: List[int]):
        self.scores = bytearray(scores)
        self.elves = elves
    
    def __next__(self):
        new_score = sum([self.scores[e] for e in self.elves])
        d1, d2 = new_score // 10, new_score % 10
        if d1: self.scores.append(d1)
        self.scores.append(d2)
        for e, v in enumerate(self.elves):
            self.elves[e] = (v + self.scores[v] + 1) % len(self.scores)
        return new_score
    
    def __len__(self):
        return len(self.scores)
    
    def __str__(self):
        return "".join([str(x) for x in self.scores])

    def __repr__(self):
        return f'scores: {self.scores}, elves: {self.elves} index: {self.idx}'
    
       
def starOne(scores: Scoreboard, input_str: str) -> str:
    input_val = int(input_str)
    while len(scores) < input_val + 10:
        next(scores)
    return str(scores)[input_val:input_val + 10]

def starTwo(scores: Scoreboard, input_str: str) -> int:
    input_ba = bytearray((int(c) for c in input_str))
    loop = 0
    while True:
        if (loop % 250_000) == 0 and input_ba in scores.scores: # check every 1/4 mil for speed
            break
        next(scores)
        loop += 1
    return scores.scores.index(input_ba)

if __name__ == "__main__":
    score_board = Scoreboard([3,7], [0,1])

    assert starOne(score_board, '5') == "0124515891"
    assert starOne(score_board, '18') == "9251071085"
    assert starOne(score_board, '2018') == "5941429882"
    print(starOne(score_board, '681901'))


    assert starTwo(score_board, '51589') == 9
    assert starTwo(score_board, '01245') == 5
    assert starTwo(score_board, '92510') == 18
    assert starTwo(score_board, '59414') == 2018
    print(starTwo(score_board, '681901'))
    