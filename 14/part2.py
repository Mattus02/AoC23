def MoveRockUp(grid: list[list[str]], column: int, row: int):
    while row > 0 and grid[row - 1][column] == '.':
        grid[row - 1][column] = 'O'
        grid[row][column] = '.'
        row -= 1

def MoveRockLeft(grid: list[list[str]], column: int, row: int):
    while column > 0 and grid[row][column - 1] == '.':
        grid[row][column - 1] = 'O'
        grid[row][column] = '.'
        column -= 1

def MoveRockDown(grid: list[list[str]], column: int, row: int):
    while row < len(grid) - 1 and grid[row + 1][column] == '.':
        grid[row + 1][column] = 'O'
        grid[row][column] = '.'
        row += 1

def MoveRockRight(grid: list[list[str]], column: int, row: int):
    while column < len(grid[0]) - 1 and grid[row][column + 1] == '.':
        grid[row][column + 1] = 'O'
        grid[row][column] = '.'
        column += 1

def TiltGrid(grid: list[list[str]]):
    # Tilt up
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][column] == 'O':
                MoveRockUp(grid, column, row)
    # Tilt left
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][column] == 'O':
                MoveRockLeft(grid, column, row)
    # Tilt Down
    for column in range(len(grid[0])):
        for row in reversed(range(len(grid))):
            if grid[row][column] == 'O':
                MoveRockDown(grid, column, row)
    # Tilt right
    for column in reversed(range(len(grid[0]))):
        for row in range(len(grid)):
            if grid[row][column] == 'O':
                MoveRockRight(grid, column, row)

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

    # Generate some data
    SAMPLE_AMOUNT = 200
    history = []
    for _ in range(SAMPLE_AMOUNT):
        TiltGrid(grid)
        load = CalcLoad(grid)
        history.append(load)

    # Find recurring pattern
    patternStartIndex = 0
    pattern = []
    for i in range(SAMPLE_AMOUNT):
        foundPattern = False
        for j in range(1, SAMPLE_AMOUNT):
            if (SAMPLE_AMOUNT - i) // j <= 1:
                break
            sequences = []
            start = i
            end = i + j
            while end <= SAMPLE_AMOUNT:
                sequences.append(history[start:end])
                start += j
                end += j
            if all(sequence == sequences[0] for sequence in sequences):
                print(f"Sequence found at index {i} with length {j}")
                print(sequences[0])
                patternStartIndex = i
                pattern = sequences[0]
                foundPattern = True
                break
        if foundPattern:
            break

    answer = pattern[(1000000000 - 1 - patternStartIndex) % len(pattern)]
    print(f"answer is: {answer}")

main()