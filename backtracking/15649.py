import sys
from itertools import combinations
sys.stdin = open('../기타/input.txt', 'r')

# n,m = map(int, sys.stdin.readline().split())
# comb = combinations(range(1,n+1), m)
# for x in comb:
#     print(*x)


n,m = map(int, sys.stdin.readline().split())
ret = []	# stack
def dfs():
    if len(ret) == m:	# 탈출 조건(ret 길이가 m 되면 출력)
        print(*ret)
        return
    for i in range(1,n+1):
        if not ret or (ret and i > ret[-1]):  # 가지치기(pruning)
            ret.append(i)
            dfs()
            ret.pop()
dfs()