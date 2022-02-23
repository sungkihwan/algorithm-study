import sys
from collections import Counter
sys.stdin = open('../기타/input.txt', 'r')

n = input()

n = sorted(n, reverse=True)

print(''.join(n))
