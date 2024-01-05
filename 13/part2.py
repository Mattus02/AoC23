def rowDiff(grid: list[str], up: int, down: int) -> int:
    diff = 0
    for c in range(len(grid[0])):
        if grid[up][c] != grid[down][c]:
            diff += 1
    return diff

def columnDiff(grid: list[str], left: int, right: int) -> bool:
    diff = 0
    for r in range(len(grid)):
        if grid[r][left] != grid[r][right]:
            diff += 1
    return diff

def isHorisontalReflectionOffByOne(grid: list[str], row: int) -> bool:
    offset = 0
    totalRowDiff = 0
    while (row - offset) >= 0 and (row + offset + 1) < len(grid):
        totalRowDiff += rowDiff(grid, row - offset, row + offset + 1)
        offset += 1
    return totalRowDiff == 1

def isVerticalReflectionOffByOne(grid: list[str], column: int) -> bool:
    offset = 0
    totalColumnDiff = 0
    while (column - offset) >= 0 and (column + offset + 1) < len(grid[0]):
        totalColumnDiff += columnDiff(grid, column - offset, column + offset + 1)
        offset += 1
    return totalColumnDiff == 1

def solvePattern(grid: list[str]) -> int:
    for c in range(len(grid[0]) - 1):
        if isVerticalReflectionOffByOne(grid, c):
            return c + 1
    for r in range(len(grid) - 1):
        if isHorisontalReflectionOffByOne(grid, r):
            return (r + 1) * 100
    print("finna return 0")
    return 0

def main():
    file = open("sample_input.txt")
    content = file.read()
    patterns = content.split("\n\n")
    sum = 0
    for pattern in patterns:
        sum += solvePattern(pattern.split('\n'))
    print(sum)

main()