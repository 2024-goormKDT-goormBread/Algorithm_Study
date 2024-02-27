# 체스판 나이트가 몇 번 움직여야 이 칸으로 이동할 수 있을까?
# 각 테스트 케이스 나이트의 최소 이동 횟수
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs():
    dq = deque()
    # 현재 위치에서 시작
    dq.append((cnt_x, cnt_y))

    while dq:
        x, y = dq.popleft()
        # 가고자 하는 위치에 도착하면 return.
        if x == wtg_x and y == wtg_y:
            return chess[x][y]
        # 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and chess[nx][ny] == 0:
                # 인덱스 값 자체를 value로 활용
                chess[nx][ny] = chess[x][y] + 1
                dq.append((nx,ny))


T = int(input())
result = 0
for _ in range(T):
    I = int(input())
    # 현재 위치
    cnt_x, cnt_y = map(int, input().split())
    # 도착 위치
    wtg_x, wtg_y = map(int, input().split())
    # 체스판 생성
    chess = [[0] * I for i in range(I)]
    # 시작 위치 값 정의
    chess[cnt_x][cnt_y] = 0
    print(bfs())
