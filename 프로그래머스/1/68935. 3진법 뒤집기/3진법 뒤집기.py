stk = []

def three(n):
    if n//3 > 0:
        three(n//3)
    stk.append(n%3)
    
def solution(n):
    answer = 0
    tmp = []
    three(n)
    
    while(stk):
        tmp.append(stk.pop())
    
    k = len(tmp)
    for i in range (len(tmp)):
        answer += 3 ** (k-1) * tmp[i]
        k -= 1
    
    return answer