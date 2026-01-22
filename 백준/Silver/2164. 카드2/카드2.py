from collections import deque

n = int(input())
que = deque()
for i in range (n):
    que.append(i+1)

for _ in range (n-1):
    que.popleft()
    que.append(que.popleft())
print(que.pop())