def solution(number, k):
    stk = []
    for i in number:
        while stk and stk[-1] < i and k>0:
            k-=1
            stk.pop()
        stk.append(i)
        print(stk)
    return "".join(stk)

print(solution("1231234",3))