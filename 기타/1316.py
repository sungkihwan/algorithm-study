import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
count = 0

for i in range(n):
    checker = {}
    read = sys.stdin.readline().strip()
    cur = read[0]
    for i in read:
        if i in checker:
            count += 1
            break
        if i != cur:
            checker[cur] = True
        cur = i

print(n - count)