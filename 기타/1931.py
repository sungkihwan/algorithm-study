import sys
from math import ceil
sys.stdin = open('input.txt', 'r')

n = int(input())
result = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
result = sorted(result, key=lambda x:(x[1],x[0]))

print(result)

end_time = 0
ans = 0
for time in result:
    if end_time <= time[0]:
        end_time = time[1]
        ans += 1
print(ans)

