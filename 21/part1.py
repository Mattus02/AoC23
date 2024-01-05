def InsertNewGardenPlots(grid, plot, newGardenPlots):
    r, c = plot
    if r > 0 and grid[r - 1][c] != '#':
        newGardenPlots.add((r - 1, c))
    if r < len(grid) - 1 and grid[r + 1][c] != '#':
        newGardenPlots.add((r + 1, c))
    if c > 0 and grid[r][c - 1] != '#':
        newGardenPlots.add((r, c - 1))
    if c < len(grid[0]) - 1 and grid[r][c + 1] != '#':
        newGardenPlots.add((r, c + 1))

def TakeSteps(grid, gardenPlots):
    newGardenPlots = set()
    for plot in gardenPlots:
        InsertNewGardenPlots(grid, plot, newGardenPlots)
    return newGardenPlots

# Main
grid = open('sample_input.txt', 'r').read().splitlines()
gardenPlots = set()
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == 'S':
            gardenPlots.add((r, c))
for _ in range(64):
    gardenPlots = TakeSteps(grid, gardenPlots)
print(len(gardenPlots))