import sys
sys.stdin = open('../기타/input.txt', 'r')

N = int(input())
result = 666
while N != 0:
    if '666' in str(result):
        N = N-1
        if N == 0:
            break
    result = result + 1
print(result)