import sys
from itertools import combinations
sys.stdin = open('../기타/input.txt', 'r')

st = input()
a = [st[i:] for i in range(len(st))]
a.sort()

for i in range(len(st)):
    print(a[i])