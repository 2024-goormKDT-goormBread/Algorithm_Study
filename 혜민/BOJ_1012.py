import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 적절한 값으로 설정

T = int(input())

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  #위치가 그래프를 벗어났다면 False
        return False
    if graph[x][y] == 1:       #배추가 있다면 0으로 방문처리하고, 재귀함수로 상하좌우 좌표를 다시 살펴보기
        graph[x][y] = 0 
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True             #배추가 있는 곳이 다 끝났으면, 연결된 곳은 dfs로 다 방문했다는 뜻이므로 True
    return False        #배추가 없는 곳이라면 False

for _ in range(T):     
    result = 0
    n, m, cabbage = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(cabbage):    
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):             #맵을 돌면서 dfs()함수를 수행하고 True이면 result +=1
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)
