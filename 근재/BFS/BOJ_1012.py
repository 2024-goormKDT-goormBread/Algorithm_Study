from collections import deque

# 상하좌우 탐색을 위한 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # 방문 처리

    while queue:
        x, y = queue.popleft() #(a,b)를 언패킹하여 x와 y에 할당
        for i in range(4): # 상하 좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0  or ny >= m:
                continue
            if graph[nx][ny] == 1: # 탐색한 위치가 범위 내에 있고, 아직 방문하지 않았으며, 값이 1인 경우
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


for i in range(T):
    result = 0
    n, m, K = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for i in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(graph, x, y)
                result += 1
    print(result)
