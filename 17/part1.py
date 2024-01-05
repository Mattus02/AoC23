import heapq
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UNSPECIFIED = 4

class TileInfo:
    def __init__(self, row, column, distance, direction, directionCount):
        self.row = row
        self.column = column
        self.distance = distance
        self.direction = direction
        self.directionCount = directionCount
    def __lt__(self, other):
        return self.distance < other.distance
    def __eq__(self, other):
        return self.distance == other.distance

grid = [[]]

def IsValidPos(row, column) -> bool:
    return row >= 0 and row < len(grid) and column >= 0 and column < len(grid[0])

def Dijkstra(startRow, startColumn, endRow, endColumn) -> int:

    visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    pq = []
    heapq.heappush(pq, TileInfo(startRow, startColumn, 0, Direction.UNSPECIFIED, 0))

    while len(pq) > 0:

        curr = heapq.heappop(pq)
        if curr.directionCount > 3:
            continue
        row = curr.row
        column = curr.column
        distance = curr.distance
        direction = curr.direction
        directionCount = curr.directionCount

        if (direction, directionCount) in visited[row][column]:
            continue

        if row == endRow and column == endColumn:
            return distance
        
        if IsValidPos(row - 1, column) and direction != Direction.DOWN:
            newDir = Direction.UP
            newCount = directionCount + 1 if newDir == direction else 1
            heapq.heappush(pq, TileInfo(row - 1, column, distance + int(grid[row - 1][column]), newDir, newCount))

        if IsValidPos(row + 1, column) and direction != Direction.UP:
            newDir = Direction.DOWN
            newCount = directionCount + 1 if newDir == direction else 1
            heapq.heappush(pq, TileInfo(row + 1, column, distance + int(grid[row + 1][column]), newDir, newCount))

        if IsValidPos(row, column - 1) and direction != Direction.RIGHT:
            newDir = Direction.LEFT
            newCount = directionCount + 1 if newDir == direction else 1
            heapq.heappush(pq, TileInfo(row, column - 1, distance + int(grid[row][column - 1]), newDir, newCount))

        if IsValidPos(row, column + 1) and direction != Direction.LEFT:
            newDir = Direction.RIGHT
            newCount = directionCount + 1 if newDir == direction else 1
            heapq.heappush(pq, TileInfo(row, column + 1, distance + int(grid[row][column + 1]), newDir, newCount))
            
        visited[row][column].append((direction, directionCount))

    return -1

# Main
file = open("sample_input.txt", 'r')
grid = file.read().splitlines()
print(Dijkstra(0, 0, len(grid) - 1, len(grid[0]) - 1))