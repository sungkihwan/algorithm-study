import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
stack = []

for i in range(n):
    line = sys.stdin.readline().rstrip()
    if line.find('push') == 0:
        num = line.split()[1]
        stack.append(int(num))
    elif line == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif line == 'size':
        print(len(stack))
    elif line == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
