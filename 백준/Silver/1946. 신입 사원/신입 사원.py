t = int(input())
for _ in range (t):
    n = int(input())
    arr = []
    ans = 0
    for i in range (n):
        (a, b) = tuple(map(int, input().split()))
        arr.append((a, b))
    arr.sort(key=lambda x: (x[0], x[1]))
    stx = 0
    sty = arr[0][1]
    ans = 1
    for i in range (1, n):    
        if (arr[i][1] == 1):
            stx = arr[i][0]
            ans += 1
        else:
            if (stx):
                if (arr[i][0] < stx):
                    stx = arr[i][0]
                    ans += 1
            else:
                if (arr[i][1] < sty):
                    sty = arr[i][1]
                    ans += 1
    print(ans)