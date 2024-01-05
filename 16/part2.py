import sys
from enum import Enum
from copy import deepcopy

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

def CountEnergized() -> int:
    count = 0
    for row in tiles:
        for t in row:
            if len(t.dirs) > 0:
                count += 1
    return count

# Main
file = open("sample_input.txt", 'r')
grid = file.read().splitlines()
tiles = [[Tile() for _ in range(len(grid[0]))] for _ in range(len(grid))]
sys.setrecursionlimit(4000)
originalTiles = deepcopy(tiles)
bestResult = 0
# Try all columns going down
for column in range(len(grid[0])):
    tiles = deepcopy(originalTiles)
    SimulateRecursively(column, 0, Direction.DOWN)
    bestResult = max(bestResult, CountEnergized())
# Try all rows going right
for row in range(len(grid)):
    tiles = deepcopy(originalTiles)
    SimulateRecursively(0, row, Direction.RIGHT)
    bestResult = max(bestResult, CountEnergized())
# Try all columns going up
for column in range(len(grid[0])):
    tiles = deepcopy(originalTiles)
    SimulateRecursively(column, len(grid) - 1, Direction.UP)
    bestResult = max(bestResult, CountEnergized())
# Try all rows going left
for row in range(len(grid)):
    tiles = deepcopy(originalTiles)
    SimulateRecursively(len(grid[0]) - 1, row, Direction.LEFT)
    bestResult = max(bestResult, CountEnergized())
print(bestResult)