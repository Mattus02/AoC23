import sys
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Tile:
    def __init__(self):
        self.dirs = []

grid = [[]]
tiles = [[]]

def newPos(x, y, dir) -> (int, int):
    if dir == Direction.UP:
        return (x, y - 1)
    elif dir == Direction.DOWN:
        return (x, y + 1)
    elif dir == Direction.LEFT:
        return (x - 1, y)
    elif dir == Direction.RIGHT:
        return (x + 1, y)
    
def IsValidPos(x, y) -> bool:
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

# Messed up x and y, whoops...
def SimulateRecursively(x, y, dir) -> None:

    if (not IsValidPos(x, y)) or (dir in tiles[y][x].dirs):
        return
    
    tiles[y][x].dirs.append(dir)

    if grid[y][x] == '.':
        x, y = newPos(x, y, dir)
        SimulateRecursively(x, y, dir)

    elif grid[y][x] == '/':

        if dir == Direction.UP:
            SimulateRecursively(x + 1, y, Direction.RIGHT)
        elif dir == Direction.DOWN:
            SimulateRecursively(x - 1, y, Direction.LEFT)
        elif dir == Direction.LEFT:
            SimulateRecursively(x, y + 1, Direction.DOWN)
        elif dir == Direction.RIGHT:
            SimulateRecursively(x, y - 1, Direction.UP)

    elif grid[y][x] == '\\':

        if dir == Direction.UP:
            SimulateRecursively(x - 1, y, Direction.LEFT)
        elif dir == Direction.DOWN:
            SimulateRecursively(x + 1, y, Direction.RIGHT)
        elif dir == Direction.LEFT:
            SimulateRecursively(x, y - 1, Direction.UP)
        elif dir == Direction.RIGHT:
            SimulateRecursively(x, y + 1, Direction.DOWN)

    elif grid[y][x] == '|':

        if dir == Direction.RIGHT or dir == Direction.LEFT:
            SimulateRecursively(x, y - 1, Direction.UP)
            SimulateRecursively(x, y + 1, Direction.DOWN)
        else:
            x, y = newPos(x, y, dir)
            SimulateRecursively(x, y, dir)

    elif grid[y][x] == '-':

        if dir == Direction.UP or dir == Direction.DOWN:
            SimulateRecursively(x - 1, y, Direction.LEFT)
            SimulateRecursively(x + 1, y, Direction.RIGHT)
        else:
            x, y = newPos(x, y, dir)
            SimulateRecursively(x, y, dir)

# Main
file = open("sample_input.txt", 'r')
grid = file.read().splitlines()
tiles = [[Tile() for _ in range(len(grid[0]))] for _ in range(len(grid))]
sys.setrecursionlimit(4000)
SimulateRecursively(0, 0, Direction.RIGHT)
count = 0
for row in tiles:
    for t in row:
        if len(t.dirs) > 0:
            count += 1
print(count)