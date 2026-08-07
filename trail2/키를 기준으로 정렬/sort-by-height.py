import sys

n = int(sys.stdin.readline())

people = []
for _ in range(n):
    name, height, weight = sys.stdin.readline().split()

    people.append((name, int(height), int(weight)))

people.sort(key=lambda x: x[1])

for p in people:
    print(f"{p[0]} {p[1]} {p[2]}")
