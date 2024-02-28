# 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.
# 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
# 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.
# 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)
# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다.

# 출력
# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

import sys
from collections import deque

# 방향 좌표 설정
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]

def bfs(PorF, queue): #(사람인지 구별, 큐)
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if data[nx][ny] == '.' or data[nx][ny] == '@': # data의 좌표가 빈공간이거나, 사람의 시작점일 경우
                    if visit[nx][ny] > cnt + 1: 
                        visit[nx][ny] = cnt + 1 
                        queue.append((nx, ny, visit[nx][ny]))
            
            elif PorF == 'P': # 사람일 경우
                print(cnt + 1) 
                return
    
    if PorF == 'P':
        print('IMPOSSIBLE')


                         
T = int(sys.stdin.readline())
for test_case in range(T):
    W, H = list(map(int, sys.stdin.readline().split()))
    data = [[0 for _ in range(W)]for _ in range(H)] # 건물 크기의 빈 리스트 생성
    visit = [[1000*1000 for _ in range(W)]for _ in range(H)] # 건물 방문 리스트 생성(각 칸 1000*1000 설정)
    Fire_queue, Person_queue = deque(), deque() #불 데크와 사람 데크를 따로 생성
    
    for i in range(H):
        D = sys.stdin.readline()
        for j in range(W):
            data[i][j] = D[j]
            
            if D[j] == '@': # 시작점일경우
                Person_queue.append((i, j, 0)) # 사람 데크에 추가 
                
            elif D[j] == '*': # 불 일경우
                visit[i][j] = 0 # visit 리스트에 불의 시작점 설정
                Fire_queue.append((i, j, 0))  # 불 데크에 추가
    
    # 불 경로 먼저 설정 후 사람 설정
    bfs('F', Fire_queue) 
    bfs('P', Person_queue)
    print(visit)
    