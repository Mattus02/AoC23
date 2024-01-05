class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __add__(self, other):
        return Point(self.r + other.r, self.c + other.c)

vector = {
    'U': Point(-1,  0),
    'D': Point( 1,  0),
    'L': Point( 0, -1),
    'R': Point( 0,  1)
}

def GetRightVector(dir) -> Point:
    if dir == 'U':
        return vector['R']
    if dir == 'D':
        return vector['L']
    if dir == 'L':
        return vector['U']
    if dir == 'R':
        return vector['D']

def FillToTheRight(p, dir, grid):
    v = GetRightVector(dir)
    p += v
    while grid[p.r][p.c] != '#':
        grid[p.r][p.c] = 'x'
        p += v

# Main
file = open("sample_input.txt", 'r')
SIZE = 801
grid = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
curr = Point(SIZE // 2, SIZE // 2)
grid[curr.r][curr.c] = '#'
instructions = file.read().splitlines()
for line in instructions:
    dir, steps, color = line.split(' ')
    steps = int(steps)
    while steps:
        curr += vector[dir]
        grid[curr.r][curr.c] = '#'
        steps -= 1

curr = Point(SIZE // 2, SIZE // 2)
for line in instructions:
    dir, steps, color = line.split(' ')
    steps = int(steps)
    while steps:
        curr += vector[dir]
        FillToTheRight(curr, dir, grid)
        steps -= 1

count = 0
for r in grid:
    for c in r:
        if c == '#' or c == 'x':
            count += 1
print(count)