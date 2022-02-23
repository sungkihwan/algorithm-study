import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
ans = []

for i in range(n):
    ans.append(sys.stdin.readline().strip())

ans = sorted(set(ans), key=lambda x: (len(x), x))

for i in ans:
    print(i)