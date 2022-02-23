import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())

for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    q = deque(enumerate(list(map(int, sys.stdin.readline().split()))))

    priority = max(q, key=lambda x:x[1])[1]
    count = 0

    while q:
        cur = q.popleft()

        if cur[1] == priority:
            count += 1
            if cur[0] == m:
                print(count)
                break
            priority = max(q, key=lambda x:x[1])[1]
        else:
            q.append(cur)