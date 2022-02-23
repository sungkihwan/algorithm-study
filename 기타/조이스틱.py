def solution(name):
    answer = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    return answer

print(solution("JEROEN"))