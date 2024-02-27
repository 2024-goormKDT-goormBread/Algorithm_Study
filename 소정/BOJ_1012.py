# < 문제 >
# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있다. 
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

# < 입력 >
# 테스트 케이스의 개수 T
# 배추밭 가로길이 M(1 ≤ M ≤ 50), 세로길이 N(1 ≤ N ≤ 50),배추가 심어져 있는 개수 K(1 ≤ K ≤ 2500)
# 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)

# < 출력 >
# 최소의 배추흰지렁이 마리 수

from collections import deque

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 정의
def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	
	while queue:
		x, y = queue.popleft()
		# 현재 노드 방문 처리
		graph[x][y] = 0

		# 현재 위치에서 4가지 방향으로의 위치 확인
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			# 배추밭을 벗어난 경우 무시
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
		
			# 배추가 아닌 경우 무시
			if graph[nx][ny] == 0:
				continue
		
			# 해당 배추를 처음 방문하는 경우에만 큐 삽입 및 방문 처리
			if graph[nx][ny] == 1:
				queue.append((nx, ny))
				graph[nx][ny] = 0 # 시간초과 해결 : 중복 방문의 경우 방지


# 테스트 케이스 개수 입력 받기
t = int(input())

for _ in range(t):
	# 베추 밭 정보 입력 받기 
	n, m, k = map(int, input().split())

	# 2차원 리스트의 배추 밭 위치 정보 입력 받기
	graph = [[0] * m for _ in range(n)]
	for _ in range(k):
		x, y = map(int, input().split())
		graph[x][y] = 1

	# 모든 노드(위치)에 대하여 지렁이 수 확인
	result = 0
	for i in range(n):
		for j in range(m):
			# 현재 위치에서 BFS 수행
			if graph[i][j] == 1:
				bfs(i, j)
				result += 1

	# 총 지렁이 수 출력
	print(result)
