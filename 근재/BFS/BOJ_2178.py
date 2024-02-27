# 미로에서 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸 수를 구하는
# 프로그램 작성 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동 가능
# 칸을 셀 때에는 시작 위치와 도착 이치도 포함

# 최소 칸수인데 중간에 길이 끊긴다면?

from collections import deque

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
result = 0  # 결과 저장할 변수

def bfs(graph, a, b):
    dq = deque()
    dq.append((a, b))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < N and 0 <= dy < M and graph[dx][dy] == 1:
                dq.append((dx, dy))
                graph[dx][dy] = graph[x][y] + 1
    return graph[N-1][M-1]


N, M = map(int, input().split())  # N x M 미로
graph = [] # N x M graph 생성

for i in range(N):
    graph.append(list(map(int, input())))

for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            result = bfs(graph, x, y)
print(result)

# x,y:  0 0, 1 0, 2 0, 3 0, 3 1, 3 2, 2 2, 1 2, 0 2, 0 3, 0 4, 0 5, 1 4, 2 4,
# ,2 5, 3 4, 3 5
# x,y:  0 0, 0 1, 1 0, 1 1, 2 0, 2 1, 3 0, 2 2, 3 1, 2 3, 3 2, 2 4, 3 3, 1 3,2 5,
# ,1 4, 0 3, 3 5, 0 4

