from typing import List, Tuple, NamedTuple, Dict
from enum import Enum

def getInput() -> List[str]:
    with open("./inputs/day13Test.txt", "r") as f:
        out = list(map(int, f.readline().split()))
    return out

Direction = Enum('Direction', ['UP','DOWN','LEFT','RIGHT','UPLEFT','UPRIGHT'])
Tile = Enum('Tile', ['HORIZONTAL','VERTICAL','INTERSECTION','F_SLASH','B_SLASH'])
Turn = Enum('Turn', ['LEFT','RIGHT','STRAIGHT'])
Position = NamedTuple('Position', [('x', int) , ('y', int)])
Cart_Directions = {
    '^': (Direction.UP, Tile.VERTICAL),
    'v': (Direction.DOWN, Tile.VERTICAL),
    '<': (Direction.LEFT, Tile.HORIZONTAL),
    '>': (Direction.RIGHT, Tile.HORIZONTAL)
}
Tile_Directions = {
    '|': Tile.VERTICAL,
    '-': Tile.HORIZONTAL,
    '+': Tile.INTERSECTION,
    '/': Tile.F_SLASH,
    '\\': Tile.B_SLASH
}
Cart_Advance = {
    Direction.UP: (0, -1),
    Direction.DOWN: (0, 1),
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0)
}

class Cart:
    def __init__(self, posX, posY, direction, turn=Turn.LEFT):
        self.x, self.y = (posX, posY)
        self.direction = direction
        self.turn = turn
        self.crashed = False
    
    def move(self, track):
            advDirection = Cart_Advance[self.direction]
            self.x, self.y = (self.x + advDirection[0], self.y + advDirection[1])
            print(f'moving: {self.direction}... {self}')
            if track[self.x, self.y] == Tile.INTERSECTION:
                pass
            elif track[self.x, self.y] == Tile.F_SLASH and self.direction == Direction.UP:
                self.direction = Direction.RIGHT
            elif track[self.x, self.y] == Tile.F_SLASH and self.direction == Direction.DOWN:
                self.direction = Direction.LEFT
            elif track[self.x, self.y] == Tile.B_SLASH and self.direction == Direction.UP:
                self.direction = Direction.LEFT
            elif track[self.x, self.y] == Tile.B_SLASH and self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
            elif track[self.x, self.y] == Tile.F_SLASH and self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
            elif track[self.x, self.y] == Tile.F_SLASH and self.direction == Direction.LEFT:
                self.direction = Direction.UP
            elif track[self.x, self.y] == Tile.B_SLASH and self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
            elif track[self.x, self.y] == Tile.B_SLASH and self.direction == Direction.LEFT:
                self.direction = Direction.UP
            

    def __repr__(self):
        return f'{self.x}, {self.y} {self.direction}/{self.turn} crashed:{self.crashed}'

class Track:
    def __init__(self):
        self.carts: List[Cart] = []
        self.grid: Dict[Position, Tile] = {}
        with open("./inputs/day13Test.txt", "r") as f:
            for y, line in enumerate(f.readlines()):
                for x, c in enumerate(line):
                    if c in Cart_Directions:
                        cart_dir, t = Cart_Directions[c]
                        self.carts.append(Cart(x,y,cart_dir))
                        self.grid[x, y] = t
                        continue
                    if c in Tile_Directions:
                        self.grid[x, y] = Tile_Directions[c]
                    
t = Track()
        
def starOne():
    pass

def starTwo() -> int:
    pass

if __name__ == "__main__":
    pass
    # inputList = getInput()
    # #print(inputList)
    # starOneOut = starOne(inputList)
    # print(starOneOut)
    # starTwoOut = starTwo(dependancies)
    # print(starTwoOut)