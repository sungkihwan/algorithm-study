import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
dq = deque()

for i in range(n):
    order = sys.stdin.readline().rstrip()

    if order.find('push_front') == 0:
        dq.appendleft(order.split()[1])
    elif order.find('push_back') == 0:
        dq.append(order.split()[1])
    elif order == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif order == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(dq))
    elif order == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif order == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)