#from typing import set
SAMPLE="""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

def read_input_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        inp: str = f.read().strip()
    return inp

def create_orbit_map(inp: str) -> dict:
    return dict(reversed(x.split(')')) for x in inp.splitlines())

def traverse_from_planet(orbit_map: dict, dest: str) -> set:
    orbits: set = set()
    while 1:
        if dest == 'COM':
            return orbits
        orbits.add(dest)
        dest = orbit_map[dest]

def starOne(inp: str) -> int:
    orbit_map: dict = create_orbit_map(inp)
    return sum( [ len( traverse_from_planet(orbit_map, x) ) for x in orbit_map.keys() ] )

def starTwo(inp: str) -> int:
    orbit_map: dict = create_orbit_map(inp)
    you: set = traverse_from_planet(orbit_map, 'YOU')
    santa: set = traverse_from_planet(orbit_map, 'SAN')
    return len(you ^ santa) - 2

if __name__ == "__main__":
    assert(starOne(SAMPLE) == 42)
    inp: str = read_input_file('./inputs/day06.txt')
    print(f'Part 1: {starOne(inp)}\nPart 2: {starTwo(inp)}')