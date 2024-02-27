# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# 예를 들어, 그림이 아래와 같은 경우에

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
# 둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.


import sys
sys.setrecursionlimit(1000000) #재귀함수 최대 깊이 설정

N = int(sys.stdin.readline())
data = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)] # 각 칸마다 False값이 들어있는 N * N 배열 설정

d = [(0,1), (0, -1), (1,0), (-1,0)] # 방향 설정
def dfs(x, y):
    visited[y][x] = True 
    color = data[y][x]
    for dx, dy in d: # 동서남북 탐색
        X, Y = x + dx, y + dy
        if (0 <= X < N) and (0 <= Y < N): # 범위 내에 있고
            if visited[Y][X] == False and data[Y][X] == color: # 방문한 적이 없고 색이 같은 경우
                dfs(X, Y) # 탐색
            
cnt1, cnt2 = 0, 0

for y in range(N): # 적록색약이 아닌 사람인 경우
    for x in range(N):
        if visited[y][x] == False:
            dfs(x,y)
            cnt1 += 1

for y in range(N): # 빨강과 초록을 구분할 수 없는 케이스 설정
    for x in range(N):
        if data[y][x] == 'G':
            data[y][x] = 'R'
visited = [[False] * N for _ in range(N)] # visited 초기화

for y in range(N): # 적록색약인 사람인 경우
    for x in range(N):
        if visited[y][x] == False:
            dfs(x,y)
            cnt2 += 1

print(cnt1, cnt2)
