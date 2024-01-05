def HashOf(content: str) -> int:
    sum = 0
    for ch in content:
        sum += ord(ch)
        sum *= 17
        sum %= 256
    return sum

def main():

    file = open("sample_input.txt", 'r')
    sequence = file.read().split(',')
    boxes = [[] for _ in range(256)]

    for s in sequence:
        if s[-1] == '-':
            label = s[0:-1]
            box = HashOf(label)
            idx = -1
            for i in range(10):
                if (label, i) in boxes[box]:
                    idx = boxes[box].index((label, i))
                    break
            if idx != -1:
                del(boxes[box][idx])
        else:
            splitted = s.split('=')
            label = splitted[0]
            focalLength = ord(splitted[1]) - ord('0')
            box = HashOf(label)
            idx = -1
            for i in range(10):
                if (label, i) in boxes[box]:
                    idx = boxes[box].index((label, i))
                    break
            if idx == -1:
                boxes[box].append((label, focalLength))
            else:
                del(boxes[box][idx])
                boxes[box].insert(idx, (label, focalLength))

    sum = 0
    for i, box in enumerate(boxes):
        for j, t in enumerate(box):
            sum += (i + 1) * (j + 1) * t[1]

    print(boxes)
    print(sum)

main()