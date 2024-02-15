from collections import deque
import sys

queue = deque()
n = int(input())
ans = []

# 프로세스 시작
for _ in range(n):
    x = sys.stdin.readline().strip().split()
    if x[0] == 'push':
        queue.append(x[1])
    elif x[0] == 'pop':
        ans.append(queue.popleft()) if queue else ans.append('-1')
    elif x[0] == 'size':
        ans.append(len(queue))
    elif x[0] == 'empty':
        ans.append('0') if queue else ans.append('1')
    elif x[0] == 'front':
        ans.append(queue[0]) if queue else ans.append('-1')
    elif x[0] == 'back':
        ans.append(queue[-1]) if queue else ans.append('-1')

# 결과 출력
for i in ans:
    print(i)
