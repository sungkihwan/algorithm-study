# import sys
# sys.stdin = open('input.txt', 'r')
# import numpy as np
# import time
#
# starttime = time.time_ns()
# n = int(input())
# tmp = []
#
# for i in range(n):
#     tmp.append(int(sys.stdin.readline()))
#
# result = np.sort(tmp, axis=- 1, kind=None, order=None)
#
# for i in range(n):
#     print(result[i])
# endtime = time.time_ns()
#
# print(f"result time : {endtime - starttime}.10f")

import sys

n = int(sys.stdin.readline())
tmp = []

for i in range(n):
    tmp.append(int(sys.stdin.readline()))

tmp.sort()

for i in range(n):
    sys.stdout.write(tmp[i])
