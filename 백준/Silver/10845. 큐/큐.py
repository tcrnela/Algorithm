import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range (n):
    a = input().strip()
    if " " in a:
        b, c = a.split()
        q.append(int(c))
    elif a == "front":
        print(-1 if len(q) == 0 else q[0])
    elif a == "back":
        print(-1 if len(q) == 0 else q[-1])
    elif a == "size":
        print(len(q))
    elif a == "empty":
        print(1 if len(q) == 0 else 0)
    elif a == "pop":
        print(-1 if len(q) == 0 else q.popleft())