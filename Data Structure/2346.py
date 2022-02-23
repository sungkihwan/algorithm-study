import sys
sys.stdin = open('input.txt', 'r')
from collections import Counter

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
t = [False] * n
t[0] = True
result = [1]

cur = 0

for i in range(n-1):
    o = l[cur]

    if o < 0:
        while o != 0:
            cur -= 1
            o += 1
            if cur == -1:
                cur = n - 1

            if t[cur]:
                o -= 1

        t[cur] = True
        result.append(cur+1)
    else:
        while o != 0:
            cur += 1
            o -= 1
            if cur == n:
                cur = 0

            if t[cur]:
                o += 1

        t[cur] = True
        result.append(cur + 1)

print(*result)