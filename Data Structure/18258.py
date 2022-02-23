import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
q = deque()

for i in range(n):
    c = sys.stdin.readline().rstrip()
    if c.find("push") == 0:
        q.append(c.split()[1])
    elif c == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c == "size":
        print(len(q))
    elif c == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif c == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)