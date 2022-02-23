import sys
sys.stdin = open('input.txt', 'r')

a, b = input().split(' ')
lenA = len(a)
lenB = len(b)
count = 50

if lenA == lenB:
    count = 0
    for i in range(lenB):
        if a[i] != b[i]:
            count += 1

for i in range(lenB - lenA + 1):
    countCur = 0
    for j in range(i, lenA + i):
        if a[j - i] != b[j]:
            countCur += 1
    count = min(count, countCur)

print(count)
