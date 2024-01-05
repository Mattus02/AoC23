def MoveRockUp(grid: list[list[str]], column: int, row: int):
    while row > 0 and grid[row - 1][column] == '.':
        grid[row - 1][column] = 'O'
        grid[row][column] = '.'
        row -= 1

def TiltGrid(grid: list[list[str]]):
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][column] == 'O':
                MoveRockUp(grid, column, row)

def CalcLoad(grid: list[str]) -> int:
    l = len(grid)
    sum = 0
    for i, row in enumerate(grid):
        for j in row:
            if j == 'O':
                sum += (l - i)
    return sum

def main():
    file = open("sample_input.txt", 'r')
    grid = [list(string) for string in file.read().split('\n')]
    TiltGrid(grid)
    print(CalcLoad(grid))

main()