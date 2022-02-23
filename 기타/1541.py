import sys
sys.stdin = open('input.txt', 'r')

st = input()
plus = []
minus = []
num = ""
sign = 1

for i in st:
    if i.isdigit():
        num += i
    elif i == "+":
        if sign == 1:
            plus.append(int(num))
        else:
            minus.append(int(num))
        num = ""
    else:
        if sign == 1:
            plus.append(int(num))
            sign *= -1
        else:
            minus.append(int(num))
        num = ""

if sign == 1:
    plus.append(int(num))
else:
    minus.append(int(num))

result = sum(plus) - sum(minus)

print(plus)
print(minus)
print(result)


