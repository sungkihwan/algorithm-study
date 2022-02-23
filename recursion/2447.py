import time
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("../기타/input.txt", "r")

N = int(sys.stdin.readline())

def makeStar(N):
    if N == 3:
        return ['***', '* *', '***']

    subStars = makeStar(N//3)
    stars = []

    for S in subStars:
        stars.append(S*3)
    for S in subStars:
        stars.append(S+' '*len(subStars)+S)
    for S in subStars:
        stars.append(S*3)

    return stars

start = time.time_ns()
print('\n'.join(makeStar(N)))
end = time.time_ns()

print(f"{end - start:.10f} sec")

