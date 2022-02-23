length = 10000
self = [True] * (length+1)
result = []

for i in range(1, length+1):
    num = i
    for j in str(i):
        num += int(j)

    if num < len(self):
        self[num] = False

for i in range(1, len(self)):
    if self[i]:
        print(i)

