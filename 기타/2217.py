import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
l = sorted([int(sys.stdin.readline()) for i in range(n)], reverse=True)

result = 0

for i in range(1, n + 1):
    cur = i * l[i - 1]
    result = result if result > cur else cur

print(result)