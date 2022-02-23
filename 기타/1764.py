import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split(' '))
d = {}

result = []

for i in range(n):
    x = sys.stdin.readline().strip()
    d[x] = x

for i in range(m):
    y = sys.stdin.readline().strip()
    if y in d:
        result.append(y)

result.sort()

print(len(result))
for i in result:
    print(i)
