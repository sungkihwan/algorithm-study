import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
l = sorted(list(map(int, sys.stdin.readline().split())))

cur = 0
result = 0

for i in range(n):
    result += cur + l[i]
    cur += l[i]

print(result)