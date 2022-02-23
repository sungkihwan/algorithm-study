import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

for i in range(n):
    read = sys.stdin.readline().strip()
    if len(read) % 2 != 0:
        print('NO')
        continue

    stack = []
    result = 'YES'

    if ")" not in read:
        print('NO')
        continue

    for i in read:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                result = 'NO'
            else:
                stack.pop()

    if stack:
        result = 'NO'

    print(result)







