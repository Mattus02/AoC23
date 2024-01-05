import strutils, sequtils

func getPossibility(original: string, questionmarkCount: int, n: int): string =
    var binString = n.toBin(questionmarkCount)
    for i in 0 ..< len(binString):
        if binString[i] == '1':
            binString[i] = '#'
        else:
            binString[i] = '.'
    var copy = original
    var idx = 0
    for i in 0 ..< len(copy):
        if copy[i] == '?':
            copy[i] = binString[idx]
            idx += 1
    return copy

func isPossible(tmp: string, groups: seq[int]): bool =
    if count(tmp, '#') != groups.foldl(a + b):
        return false
    var curr = 0
    var idx = 0
    while true:
        idx = find(tmp, '#'.repeat(groups[curr]), idx)
        if idx == -1:
            return false
        idx += groups[curr]
        curr += 1
        if curr >= len(groups):
            break
        if idx >= len(tmp) or tmp[idx] != '.':
            return false
    if find(tmp, '#', idx) != -1:
        return false
    return true

func pow2(n: int): int =
    var res = 1
    for i in 0 ..< n:
        res *= 2
    return res

proc solveLine(line: string): int =
    let splitted = line.split(" ")
    let original = splitted[0]
    var groups = splitted[1].split(",").mapIt(parseInt(it))
    let questionmarkCount = count(original, '?')
    var sum = 0
    for i in 0 ..< pow2(questionmarkCount):
        let tmp = getPossibility(original, questionmarkCount, i)
        if isPossible(tmp, groups):
            sum += 1
    return sum

proc main(): void =
    var sum = 0
    for line in readFile("sample_input.txt").splitLines():
        let tmp = solveLine(line)
        sum += tmp
        echo tmp
        echo "---------"
    echo sum

main()