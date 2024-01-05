class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __mul__(self, otherInteger):
        return Point(self.x * otherInteger, self.y * otherInteger)
    def __str__(self):
        return f"({self.x}, {self.y})"

vector = [Point(1,  0), Point(0, -1), Point(-1,  0), Point(0,  1)]

def PolygonArea(vertices):
    sum1 = 0
    sum2 = 0
    for i in range(len(vertices) - 1):
        sum1 += vertices[i].x * vertices[i+1].y
        sum2 += vertices[i].y * vertices[i+1].x
    sum1 += vertices[len(vertices) - 1].x * vertices[0].y   
    sum2 += vertices[0].x * vertices[len(vertices)-1].y   
    area = abs(sum1 - sum2) // 2
    return area

# Main
file = open("sample_input.txt", 'r')
curr = Point(0, 0)
vertices = []
totalDist = 0
for line in file.read().splitlines():
    rgb = line.split(' ')[2][2:8]
    dist = int(rgb[0:5], 16)
    totalDist += abs(dist)
    v = vector[int(rgb[-1])]
    curr += v * dist
    vertices.append(curr)
print(PolygonArea(vertices) + totalDist // 2 + 1)