# < 문제 >
# 1 = 익은 토마토
# 0 = 익지 않은 토마토
# -1 = 토마토가 들어있지 않은 칸

# 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력

# < 풀이 >
# 1. 3차원 배열 생성 & (상,하,좌,우,앞,뒤) 방향 설정
# 2. 입력 값 중에서 익은 토마토 = 1인 경우, 큐에 차례로 담아준다
# 	*주의* '시간'이라는 조건이 붙었기 때문에, 
#	익은 토마토 = 1을 발견할 때마다 해당 위치에서 BFS를 시작하는 것이 아니라
#	그래프를 입력 받을 때 익은 토마토 = 1이면 모두 큐에 넣은 후에 BFS를 동시에 시작해야 한다
# 3. BFS 실행
# 4. 6가지 방향의 인접해 있는 위치의 토마토 상태 확인
#	4-1. 상자를 벗어난 경우 무시
# 	4-2. 익지 않은 경우 = 0, 큐에 넣어 토마토 방문 처리하고 Day +1 
# 5. 모든 탐색이 끝난 후
#	5-1. 익지않은 토마토 = 0가 있는 경우, -1 출력
#	5-2. 저장될 때부터 모든 토마토가 익은 토마토 = 1인 경우, 0 출력
#	5-3. 두 가지 경우가 아닌 경우, 익을 때 까지 걸린 가장 큰 Day -1 출력
#		*주의* 변수 Day가 1부터 시작했으므로 최종적으로 익을 때까지 걸린 기간은 Day -1 이다.

from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
	while queue:
		x, y, z = queue.popleft()
		for i in range(6):
			nx = x + dx[i]
			ny = y + dy[i]
			nz = z + dz[i]

			if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
				continue
	
			if box[nz][nx][ny] == 0:
				queue.append((nx, ny, nz))
				box[nz][nx][ny] = box[z][x][y] + 1


m, n, h = map(int, input().split())
box = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

queue = deque()
for i in range(h):
	for j in range(n):
		for k in range(m):
			if box[i][j][k] == 1:
				queue.append((j, k, i))

bfs()

day = 0
for i in range(h):
	for j in range(n):
		for k in range(m):
			if box[i][j][k] == 0:
				print(-1)
				exit(0)
			day = max(day, box[i][j][k])

print(day - 1)
