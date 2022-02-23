import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

trees = list(map(int, input().split()))

right = max(trees)
left = 0
result = 0

while left <= right:
    mid = (left + right) // 2

    s = sum([i-mid for i in trees if i > mid])

    if s >= m:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)

