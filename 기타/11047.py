import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
l = [int(sys.stdin.readline().rstrip()) for i in range(n)]
count = 0

for i in range(n-1, -1, -1):
    count += k // l[i]
    k %= l[i]
    if k == 0:
        break

print(count)
