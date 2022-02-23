from math import ceil

def solution(progresses, speeds):
    result = []
    q = [ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]

    print(q)

    count = 0
    now = q[0]
    for i in range(1, len(q)):
        count += 1
        if now < q[i]:
            now = q[i]
            result.append(count)
            count = 0

    result.append(count + 1)
    return result

# print(solution([7, 15, 98, 6, 80, 1], [10, 7, 1, 15, 10, 80]))
# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))