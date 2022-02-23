import sys
sys.stdin = open('input.txt', 'r')

s = input()

cur = s[0]
val = 1

result = 0

for i in range(1, len(s)):
    if cur == "(" and s[i] == ")":
        val -= 1
        result += val
    elif s[i] == "(":
        val += 1
    elif s[i] == ")":
        val -= 1
        result += 1

    cur = s[i]

print(result)