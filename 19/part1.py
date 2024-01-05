m = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3
}

def IsAccepted(categories, workflows) -> bool:
    name = "in"
    while True:
        if name == 'A':
            return True
        elif name == 'R':
            return False
        rules = workflows[name]
        for rule in rules:
            if ':' not in rule:
                name = rule
                break
            condition, jumpTo = rule.split(':')
            booleanExpression = str(categories[m[condition[0]]]) + condition[1:]
            if eval(booleanExpression) == True:
                name = jumpTo
                break

# Main
file = open("sample_input.txt", 'r')
content = file.read().split("\n\n")
workflows = {}
for line in content[0].splitlines():
    splitted = line.split('{')
    name = splitted[0]
    rules = splitted[1][:-1].split(',')
    workflows[name] = rules

count = 0
for line in content[1].splitlines():
    line = line[1:-1].split(',')
    categories = [int(line[i][2:]) for i in range(4)]
    if IsAccepted(categories, workflows):
        count += sum(categories)

print(count)