from collections import deque

t = int(input())

def bfs() :
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]       #8개의 모든 이동 방향을 설정
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    queue = deque()
    queue.append((start_X, start_Y))
    while queue :
        x, y = queue.popleft()

        if x == end_X and y == end_Y :  #목적지 도착했다면 종료 
            return graph[x][y] -1 
        
        for i in range(8):      #8개의 이동 방향을 돌면서 다음 좌표로 이동 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 : #다음 위치가 좌표에 벗어나지 않고 아직 방문 안했다면
                graph[nx][ny] = graph[x][y] + 1     #다음 좌표 값에 +1
                queue.append((nx,ny))       #다음 좌표 큐에 삽입 
                
        
for _ in range(t) :
    n = int(input)
    start_X, start_Y = map(int, input().split())    #출발 좌표 입력
    end_X, end_Y = map(int, input().split())        #목적지 좌표 입력

    graph = [[0] * n for _ in range(n)]
    graph[start_X][start_Y] = 1         #출발지는 방문했으므로 1로 설정 
    print(bfs())