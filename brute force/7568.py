import sys
sys.stdin = open("../기타/input.txt", "r")

N = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [1 for _ in range(N)]

for i in range(N-1):
    for j in range(i, N):
        if L[i][0] > L[j][0] and L[i][1] > L[j][1]:
            result[j] += 1
        elif L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            result[i] += 1

print(*result)
