from collections import deque

def solution(priorities, location):
    count = 0
    dq = deque((i, x) for i, x in enumerate(priorities))

    while True:
        cur = dq.popleft()
        if any(v[1] > cur[1] for v in dq):
            dq.append(cur)
        else:
            count += 1
            if cur[0] == location:
                break

    return count

print(solution([1, 1, 9, 1, 1, 1], 0))