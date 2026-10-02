def solution(n, m):
    answer = []
    x = gcd(n, m)
    answer.append(x)
    answer.append(n*m/x)
    return answer

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

