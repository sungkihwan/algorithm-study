import sys
sys.stdin = open("../기타/input.txt", "r")

def hanoi(n, start, target, sub):
    if n == 0:
        return
    hanoi(n - 1, start, sub, target)  # 맨 아래 원반 이외의 원반들을 보조장대로 재귀적으로 옮기기
    print(start, target)  # 그 사이에 원반을 어디에서 어디로 한 번 옮길지 출력
    hanoi(n - 1, sub, target, start)  # 마지막으로, 보조장대로 옮겼던 원반들을 그 위에 얹는다.

n = int(sys.stdin.readline())
print(2 ** n - 1)  # 이동 횟수 출력
hanoi(n, 1, 3, 2)