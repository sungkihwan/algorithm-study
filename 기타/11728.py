import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
result = sorted(arr1 + arr2)

print(*result)