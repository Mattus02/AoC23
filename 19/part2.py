from copy import deepcopy

m = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3
}

flipped = {
    '<': '>=',
    '>': '<='
}

workflows = {}
allPaths = []

def InsertIntoAllPaths(currPath, condition):
    for i, path in enumerate(allPaths):
        if set(currPath).issubset(set(path)):
            allPaths[i].append(condition)
            return
    allPaths.append(deepcopy(currPath))
    allPaths[-1].append(condition)

def FindAllPaths(currPath, workflow, ruleIndex):

    rule = workflows[workflow][ruleIndex]

    if ':' not in rule:
        if len(rule) > 1:
            FindAllPaths(currPath, rule, 0)
        elif rule == 'A':
            allPaths.append(deepcopy(currPath))
        return
    
    condition, jumpTo = rule.split(':')

    if len(jumpTo) == 1:
        if jumpTo == 'A':
            InsertIntoAllPaths(currPath, condition)
    else:
        currPath.append(condition)
        FindAllPaths(deepcopy(currPath), jumpTo, 0)
        currPath.pop()
    sign = condition[1]
    condition = flipped[sign].join(condition.split(sign))
    currPath.append(condition)
    FindAllPaths(deepcopy(currPath), workflow, ruleIndex + 1)

def InsideRange(range, number) -> bool:
    return number >= range[0] and number <= range[1]

def RangeSum(ranges) -> int:
    sum = 0
    for range in ranges:
        sum += (range[1] - range[0]) + 1
    return sum
    
def CountCombinations(path) -> int:

    ranges = {
        'x': [[1, 4000]],
        'm': [[1, 4000]],
        'a': [[1, 4000]],
        's': [[1, 4000]]
    }

    for condition in path:

        attribute = condition[0]
        sign = condition[1]
        splitChar = '=' if '=' in condition else sign

        if sign == '>':

            number = int(condition.split(splitChar)[1])
            number += 1 if '=' not in condition else 0
            if InsideRange(ranges[attribute][0], number):
                ranges[attribute][0][0] = number
            else:
                ranges[attribute].append([number, 4000])
                
        elif sign == '<':

            number = int(condition.split(splitChar)[1])
            number -= 1 if '=' not in condition else 0
            if InsideRange(ranges[attribute][0], number):
                ranges[attribute][0][1] = number
            else:
                ranges[attribute].append([1, 4000])

    product = 1
    product *= RangeSum(ranges['x'])
    product *= RangeSum(ranges['m'])
    product *= RangeSum(ranges['a'])
    product *= RangeSum(ranges['s'])
    return product

# Main
file = open("sample_input.txt", 'r')
content = file.read().split("\n\n")
for line in content[0].splitlines():
    splitted = line.split('{')
    name = splitted[0]
    rules = splitted[1][:-1].split(',')
    workflows[name] = rules
FindAllPaths([], "in", 0)
combinations = 0
for path in allPaths:
    combinations += CountCombinations(path)
print(combinations)