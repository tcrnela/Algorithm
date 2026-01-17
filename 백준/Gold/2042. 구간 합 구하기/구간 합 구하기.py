import sys
input = sys.stdin.readline

def update(a, b):
    global arr
    i = a + 2**j - 1
    d = b - arr[i]
    arr[i] += d
    while(i > 1):
        arr[i//2] += d
        i //= 2

def calc(a, b):
    ans = 0
    si = a + 2**j - 1
    ei = si + b - a
        
    while(si <= ei):
        if si % 2:
            ans += arr[si]
        if not ei % 2:
            ans += arr[ei]
            
        si = (si + 1) // 2
        ei = (ei - 1) // 2

    print(ans)

n, m, k = map(int, input().split())

for i in range (30):
    if (2**i) >= n:
        j = i
        break

arr = [0] * (2 ** (j+1))

for i in range (n):
    arr[2**j + i] = int(input())

for i in range (2 ** (j+1) - 1, 1, -2):
    arr[i//2] = arr[i] + arr[i-1]

for i in range(m+k):
    a, b, c = map(int, input().split())
    if (a == 1):
        update(b, c)
    else:
        calc(b, c)