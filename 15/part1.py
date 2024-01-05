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
    sum = 0
    for s in sequence:
        sum += HashOf(s)
    print(sum)

main()