import sys
from collections import deque
sys.stdin = open("../기타/input.txt", "r")

N, M = map(int,sys.stdin.readline().split())
dp = [[0] * M for i in range(N)]
W = []
V = []

for i in range(N):
    curW, curV = map(int,sys.stdin.readline().split())
    W.append(curW)
    V.append(curV)

for i in range(1, N):
    for j in range(1, M):

        if W[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - W[i]] + V[i])


print(dp)
print(W,V)