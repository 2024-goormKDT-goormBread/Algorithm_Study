import sys
from collections import deque

n, m = map(int, input().split())
x, y, z = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = 0

# 북 : 0, 동 : 1, 남 : 2, 서 : 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs (i, j , z):
	global count
	queue = deque()
	queue.append((i, j))
	arr[i][j] = 2
	count += 1

	while queue:
		x, y = queue.popleft()
		flag = 0 
		for _ in range(4): # 반시계 방향으로 회전
			z = (z + 3) % 4 # 반시계 방향 구하기 : (z + 3) % 4
			nx = x + dx[z]
			ny = y + dy[z]
			if nx >= n or nx < 0 or ny >= m or ny < 0:
				continue
			if arr[nx][ny] == 0: # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우
				queue.append((nx, ny)) 
				arr[nx][ny] = 2
				count += 1
				flag = 1 # 반시계 방향으로 돌아갔을 때 빈칸이 있다는 것을 의미
				break

		if flag == 0: # 청소할 곳이 없다면 후진
			# 후진 위치 구하기 : graph[x-dx[z]][y-dy[z]]
			if arr[x-dx[z]][y-dy[z]] == 1: # 벽일 경우 중단
				break
			elif arr[x-dx[z]][y-dy[z]] == 2: # 방문한 경우
				queue.append((x-dx[z], y-dy[z])) 
			else:
				queue.append((x-dx[z], y-dy[z])) # 방문안한 경우
				arr[x-dx[z]][y-dy[z]] = 2
				count += 1

bfs(x, y, z)
print(count)