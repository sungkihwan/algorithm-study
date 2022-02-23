import sys
sys.stdin = open('input.txt', 'r')

cur = 0
result = []
l = []

for i in range(int(input())):
    num = int(sys.stdin.readline().rstrip())

    if cur < num:
        for i in range(cur+1, num+1):
            cur += 1
            l.append(i)
            result.append('+')
        l.pop()
        result.append('-')
    else:
        x = l.pop()
        if x != num:
            result = ['NO']
            break
        result.append('-')

for i in result:
    print(i)
