RACES = 4
file = open("input1.txt", 'r')

time = [int(i) for i in file.readline().split()[1:]]
distance = [int(i) for i in file.readline().split()[1:]]

answer = 1

for r in range(0, RACES):
    sum = 0
    for t in range(0, time[r]):
        if (time[r] - t) * t > distance[r]:
            sum += 1
    answer *= sum

print(answer)