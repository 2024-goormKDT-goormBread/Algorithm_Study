# 미로에서 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸 수를 구하는
# 프로그램 작성 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동 가능
# 칸을 셀 때에는 시작 위치와 도착 이치도 포함
from collections import deque

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
result = 0  # 결과 저장할 변수


# graph = [
# [1, 0, 1, 1, 1, 1],
# [1, 0, 1, 0, 1, 0],
# [1, 0, 1, 0, 1, 1],
# [1, 1, 1, 0, 1, 1]
# ]

def bfs(graph, a, b, result):
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0
    print(dq)
    while dq:
        x, y = dq.popleft()
        print("x,y: ",x,y)
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 1 or dy < 1 or dx >= N or dy >= M:
                continue
            if graph[dx][dy] == 1:
                dq.append((dx, dy))
                graph[dx][dy] = 0
                result += 1
    return


N, M = map(int, input().split())  # N x M 미로
graph = []  # N x M graph 생성

for i in range(N):
    graph.append(list(map(int, input())))
print(graph)
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            bfs(graph, x, y, result)
print(result)
