import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline
board = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]
b = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

dh = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)


def rotate(b):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4 - i] = b[i][j];

    return tmp


def bfs(b):
    global result
    q = deque()
    dist = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    q.append((0, 0, 0))

    while q:
        h, y, x = q.popleft()
        if (h, y, x) == (4, 4, 4):
            result = min(result, dist[4][4][4])
            if result == 12: # 가장 짧은 경로의 경우 출력 후 종료
                print(result)
                exit()
            return

        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nh < 0 or nh >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            elif b[nh][ny][nx] == 0 or dist[nh][ny][nx] != 0:
                continue
            q.append((nh, ny, nx))
            dist[nh][ny][nx] = dist[h][y][x] + 1


def dfs(d):
    global b
    if d == 5:
        if b[4][4][4]:
            bfs(b)
        return

    for i in range(4):
        if b[0][0][0]:
            dfs(d + 1)
        b[d] = rotate(b[d])


for d in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
        b[d[i]] = board[i]
    dfs(0)

if result == sys.maxsize:
    result = -1
print(result)