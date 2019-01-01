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
Cart_Advance_rev = { # poor man's bidict
    (0, -1): Direction.UP,
    (0, 1): Direction.DOWN,
    (-1, 0): Direction.LEFT, 
    (1, 0): Direction.RIGHT,
}

class Cart:
    def __init__(self, posX, posY, direction, turn=Turn.LEFT):
        self.x, self.y = (posX, posY)
        self.direction = direction
        self.turn = turn
        self.crashed = False
    
    def move(self, track_grid):
            dx, dy = Cart_Advance[self.direction]
            self.x, self.y = (self.x + dx, self.y + dy)
            #print(f'tile: {track_grid[self.x, self.y]}... {self}')
            if track_grid[self.x, self.y] == Tile.INTERSECTION:
                if self.turn == Turn.LEFT:
                    self.direction = Cart_Advance_rev[(dy, -dx)]
                    self.turn = Turn.STRAIGHT
                elif self.turn == Turn.RIGHT:
                    self.direction = Cart_Advance_rev[(-dy, dx)]
                    self.turn = Turn.LEFT
                else:
                    self.turn = Turn.RIGHT
            elif track_grid[self.x, self.y] == Tile.F_SLASH:
                self.direction = Cart_Advance_rev[(-dy, -dx)]
            elif track_grid[self.x, self.y] == Tile.B_SLASH:
                self.direction = Cart_Advance_rev[(dy, dx)]
            #print(self.direction)
            
    def __repr__(self):
        return f'({self.x}, {self.y}) dir: {self.direction} / nextTurn: {self.turn} crashed:{self.crashed}'

class Track:
    def __init__(self):
        self.carts: List[Cart] = []
        self.grid: Dict[Position, Tile] = {}
        with open("./inputs/day13.txt", "r") as f:
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

# Star 1:
cartCount = len(t.carts)
tickCount = 0
while cartCount>1:
    t.carts.sort(key=lambda x: (x.x, x.y))
    for c in t.carts:
        if c.crashed: continue
        c.move(t.grid)
        for j, other in enumerate(t.carts):
            if (other.x, other.y) == (c.x, c.y) and c is not other and not other.crashed:
                c.crashed = True
                t.carts[j].crashed = True
                cartCount -= 2
                print(f'CRASH DETECTED @ ({c.x},{c.y})   \t{cartCount} remaining.\t(tick {tickCount}).')
    tickCount += 1

# Star 2:
<<<<<<< HEAD
[print(c) for c in t.carts if not c.crashed]
=======
[c for c in t.carts if not c.crashed]
>>>>>>> 78366f7d6e0594191dae38c096923e98b68008f0
