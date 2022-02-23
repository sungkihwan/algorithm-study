import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
cards = deque([i for i in range(1, n+1)])
i = 0

while n > 1:
    if i % 2 == 0:
        n -= 1
        cards.popleft()
    else:
        cards.append(cards.popleft())

    i += 1

print(cards[0])