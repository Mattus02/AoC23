import strutils, algorithm

type Point = object
    x: int
    y: int

proc readIntoGrid(filename: string): seq[seq[char]] =

    var content = readFile(filename)
    var lines = content.splitLines()
    var res: seq[seq[char]] = @[]

    for line in lines:
        var row: seq[char] = @[]
        for numStr in line.split():
            row.add(numStr)
        res.add(row)

    return res

func distance(p1: Point, p2: Point, emptyRows: seq[int], emptyColumns: seq[int], galaxyFactor: int): int =

    var xs: seq[int] = @[p1.x, p2.x]
    var ys: seq[int] = @[p1.y, p2.y]
    xs.sort()
    ys.sort()
    var columnCount = 0
    for c in emptyColumns:
        if c > xs[0] and c < xs[1]:
            columnCount += 1
    var rowCount = 0
    for r in emptyRows:
        if r > ys[0] and r < ys[1]:
            rowCount += 1

    return (xs[1] - xs[0] - columnCount + columnCount * galaxyFactor) + (ys[1] - ys[0] - rowCount + rowCount * galaxyFactor) 

proc main(): void =

    let grid = readIntoGrid("sample_input.txt")

    var emptyRows: seq[int]
    for i, row in grid:
        if not row.contains('#'):
            emptyRows.add(i)

    var emptyColumns: seq[int]
    for c in 0 ..< len(grid):
        var isEmpty = true
        for r in 0 ..< len(grid):
            if grid[r][c] == '#':
                isEmpty = false
                break
        if isEmpty:
            emptyColumns.add(c)

    var galaxies: seq[Point]
    for r in 0 ..< len(grid):
        for c in 0 ..< len(grid[r]):
            if grid[r][c] == '#':
                galaxies.add(Point(x: c, y: r))

    var sum = 0
    for i in 0 ..< len(galaxies):
        for j in i+1 ..< len(galaxies):
            sum += distance(galaxies[i], galaxies[j], emptyRows, emptyColumns, 1_000_000)

    echo sum

main()