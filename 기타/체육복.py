def solution(n, lost, reserve):
    count = 0
    setLost = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))
    answer = n - len(setLost)

    for i in setLost:
        for idx ,j in enumerate(reserve):
            if j - i == -1 or j - i == 1:
                count += 1
                del reserve[idx]
                break

    return answer + count

print(solution(20,[16,17],[17,18]))