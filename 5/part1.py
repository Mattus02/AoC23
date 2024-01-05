import copy
import math

file = open("sample_input.txt", 'r')

seeds = [int(i) for i in (file.readline().split()[1:])]
file.readline()
file.readline()

allMaps = []
currMap = []

for line in file:
    line = line.split()
    if len(line) < 2:
        continue
    elif len(line) == 2:
        allMaps.append(copy.deepcopy(currMap))
        currMap.clear()
        continue
    currMap.append([int(i) for i in line])

allMaps.append(currMap)

minLoc = math.inf

for s in seeds:
    loc = s
    for m in allMaps:
        for mapping in m:
            if loc >= mapping[1] and loc <= mapping[1] + mapping[2]:
                loc = mapping[0] + (loc - mapping[1])
                break
    minLoc = min(minLoc, loc)

print(minLoc)