'''
한나는 해충방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
한마리라도 살고 있으면 인접한 다른 배추로 이동할 수 있어, 그 배추들역시 보호받음
한배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 인접해있는 것임.
서로 인접해있는 배추들이 몇군데에 퍼져있는지 조사하면 총 몇마리의 지렁이가 필요한지 알수 있음.

예를 들어
1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1
인 경우 최소 5마리의 배추흰지렁이가 필요하다. (0은 배추없음, 1은 배추있음)

-- 입력
첫 줄에는 테스트케이스의 개수T
다음 줄부터는 테스트케이스에 대한 내용임
  1. 배추밭의 가로길이 M(1<= M 50), 세로길이 N(1<=N<=50), 배추개수 K(1<=K<=2500)
  2. 배추개수 K에 따라, 배추의 위치 X(0<=X<M-1), Y(0<=Y<=Y-1)

-- 출력
각 테스트케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력
'''
# 
#

import sys
from collections import deque

def bfs(matrix, start_x, start_y, visited):
    # 행, 열 개수 
    rows = len(matrix)
    cols = len(matrix[0])
    
    queue = deque([(start_x, start_y)]) # 탐색을 시작할 노드 큐에 저장
    visited[start_y][start_x] = True    # 시작점 방문처리 

    while queue:                        # 큐가 빌 때까지 반복
        x, y = queue.popleft()          # 큐에서 노드를 하나 꺼냄
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 이동을 위한 벡터 정의
        for dx, dy in directions:                        # 상하좌우 인접한 노드를 확인
            nx, ny = x + dx, y + dy
            # 이동한 위치가 rows/cols범위 내이고, 방문되어지지 않은 노드가 있을 때
            if (0 <= nx < cols) and (0 <= ny < rows) and not visited[ny][nx] and matrix[ny][nx] == 1:
                # 방문 처리하고 큐에 추가
                visited[ny][nx] = True
                queue.append((nx, ny))

def countBugs(width, length, cabbages):
    # 배추가 심어진 위치를 나타내는 매트릭스와 방문 여부를 나타내는 매트릭스를 초기화
    cabbageMatrix = [[0] * width for _ in range(length)]
    visited = [[False] * width for _ in range(length)]
    for x, y in cabbages:
        cabbageMatrix[y][x] = 1
        
    count = 0    # 지렁이 개수 초기화(즉 지렁이개수는 인접한 배추 그룹의 개수와 같음)
    for x, y in cabbages:
        if cabbageMatrix[y][x] == 1 and not visited[y][x]: # 아직 방문되지 않은 배추 기준
            bfs(cabbageMatrix, x, y, visited)              # 인접한 배추가 있는지 BFS 탐색
            count += 1

    return count

def main():
    T = int(sys.stdin.readline().strip())  # 테스트케이스 개수
    for _ in range(T):
        # 배추밭 크기(가로M, 세로N), 배추개수 K, 그리고 배추들 위치( X, Y)
        M, N, K = map(int, sys.stdin.readline().strip().split())                           
        cabbages = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
        
        # 배추 위치에 따른 지렁이개수 세기
        result = countBugs(M, N, cabbages)
        sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main()