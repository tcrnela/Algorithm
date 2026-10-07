def solution(s):
    answer = ''
    c = 0
    for i in s:
        if i == ' ':
            answer += i
            c = 0
        elif c:
            answer += i.lower()
            c = 0
        else:
            answer += i.upper()
            c = 1

    return answer