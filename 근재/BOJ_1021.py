from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([i for i in range(1, N+1)])
count = 0

for i in arr:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) < len(que) / 2:
                while que[0] != i:
                    que.append(que.popleft())
                    count += 1
            else:
                while que[0] != i:
                    que.appendleft(que.pop())
                    count += 1
print(count)