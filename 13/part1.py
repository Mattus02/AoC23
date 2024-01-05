def columnsAreEqual(grid: list[str], left: int, right: int) -> bool:
    for r in range(len(grid)):
        if grid[r][left] != grid[r][right]:
            return False
    return True

def isVerticalReflection(grid: list[str], column: int) -> bool:
    offset = 0    
    while (column - offset) >= 0 and (column + offset + 1) < len(grid[0]):
        if not columnsAreEqual(grid, column - offset, column + offset + 1):
            return False
        offset += 1
    return True

def rowsAreEqual(grid: list[str], up: int, down: int) -> bool:
    return grid[up] == grid[down]

def isHorisontalReflection(grid: list[str], row: int) -> bool:
    offset = 0    
    while (row - offset) >= 0 and (row + offset + 1) < len(grid):
        if not rowsAreEqual(grid, row - offset, row + offset + 1):
            return False
        offset += 1
    return True

def solvePattern(grid: list[str]) -> int:
    for c in range(len(grid[0]) - 1):
        if isVerticalReflection(grid, c):
            return c + 1
    for r in range(len(grid) - 1):
        if isHorisontalReflection(grid, r):
            return (r + 1) * 100
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