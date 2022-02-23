import sys
from collections import Counter
sys.stdin = open('../기타/input.txt', 'r')

# list 정렬
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

# 1번
print(round(sum(arr)/n))

# 2번
print(arr[n//2])

# 3번
nums = Counter(arr).most_common(2)

if len(nums) == 2:
    if nums[0][1] > nums[1][1]:
        print(nums[0][0])
    else:
        print(nums[1][0])
else:
    print(nums[0][0])

# 4번
print(arr[-1] - arr[0])
