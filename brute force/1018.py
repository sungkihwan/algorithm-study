import sys
sys.stdin = open("../기타/input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    s = sys.stdin.readline()
    arr.append(s)

minCnt = 64
lastc = ['B', 'W']
countArr = []

for i in range(n - 7):
    for j in range(m - 7):

        for k in range(2):  # B 한번 W 한번
            count = 0
            last = lastc[k]
            for a in range(8):
                for b in range(8):
                    if arr[i + a][j + b] == last:
                        count += 1
                    if last == 'B':
                        last = 'W'
                    else:
                        last = 'B'
                if last == 'B':
                    last = 'W'
                else:
                    last = 'B'
            countArr.append(count)

print(min(countArr))