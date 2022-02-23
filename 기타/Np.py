# import sys
#
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# prefixSum = [0]
# temp = 0
#
# for i in A:
#     temp += i
#     prefixSum.append(temp)
#
# for i in range(M):
#     s, e = sys.stdin.readline().split()
#     s, e = int(s), int(e)
#     print(prefixSum[e] - prefixSum[s-1])
#
#
# import math
#
# def BinaryBit(k):
#     return int(math.log(k, 2))
#
# def findSurvivor(n):
#     bit = BinaryBit(100)
#     R = n - pow(2, bit)
#     survivor = 2 * R + 1
#     return survivor
#
# solution = findSurvivor(100)
# print("The Survivor is %d" % solution)
#
# survivors = list(range(1, 101))
# stickownerIndex = 0
#
# while len(survivors) > 1:
#     loser = (stickownerIndex + 1) % len(survivors)
#     del survivors[loser]
#     stickownerIndex = loser
#
# print("The Survivor is %d" % survivors[0])

for i in range(8000,10001):
    if i%11 == 7 and i%17 == 13 and i%23 == 19:
        print(i)

print(11*17*23)