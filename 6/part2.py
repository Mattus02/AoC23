def is_valid(n):
    return (time - n) * n > distance

file = open("input2.txt", 'r')

time = int(file.readline().split()[1])
distance = int(file.readline().split()[1])

found_lower = False
found_upper = False
curr_lower = time // 2
curr_upper = time // 2

while not found_lower and not found_upper:
    if not is_valid(curr_lower):
        found_lower = True
    if not is_valid(curr_upper):
        found_upper = True
    curr_upper = (time + curr_upper) // 2
    curr_lower = curr_lower // 2

while not is_valid(curr_lower):
    curr_lower += 1

while not is_valid(curr_upper):
    curr_upper -= 1

print(curr_upper - curr_lower + 1)