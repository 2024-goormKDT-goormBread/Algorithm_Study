'''
문제제목: 감시 (http://acmicpc.net/problem/15683)
문제요약:
    사무실에는 1~5번까지의 CCTV가 설치되어 있고, CCTV는 감시할 수 있는 방향이 4가지가 있다.
    CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
    사무실에는 벽이 있을 수 있고, CCTV는 벽을 통과할 수 없다.
    CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
    사무실의 크기와 CCTV의 위치가 주어졌을 때, CCTV가 감시할 수 없는 영역의 최소 크기를 구하는 문제
풀이방법:
    1. CCTV가 감시할 수 있는 영역을 모두 구한다.
    2. CCTV가 감시할 수 없는 영역을 구한다.
    3. CCTV가 감시할 수 없는 영역의 최소 크기를 구한다.
'''

# 주어진 위치(x, y)와 방향(directions)에 따라 CCTV 감시 영역을 설정하는 함수
def watch(x, y, directions, temp_map):
    for dx, dy in directions:
        nx, ny = x, y
        
        # 맵의 범위 안에 있고, 벽(6)을 만나지 않는 동안 반복
        while 0 <= nx < n and 0 <= ny < m and temp_map[nx][ny] != 6:
            # 현재 위치를 감시 구역으로 설정
            temp_map[nx][ny] = '#'
            
            # 다음 위치로 이동
            nx += dx
            ny += dy

# 모든 CCTV의 방향을 설정하고 최소 미감시 영역을 계산하는 재귀 함수
def dfs(depth, office, cctvs, cctv_directions):
    if depth == len(cctvs):
        return sum(row.count(0) for row in office) # 감시되지 않는 영역의 크기 계산 (0의 개수)
    
    x, y, cctv_type = cctvs[depth]
    results = []
    
    for directions in cctv_directions[cctv_type]: # CCTV 종류에 따른 감시 방향 설정
        temp_map = [row[:] for row in office]     # 사무실 정보 복사
        
        watch(x, y, directions, temp_map)         # 현재 CCTV의 감시 영역 설정
        results.append(dfs(depth + 1, temp_map))  # 다음 CCTV로 넘어가기
        
    # 가능한 모든 설정의 결과 중 최소값 반환
    return min(results)

def solve():
    global n, m, cctv_directions
    
    # 사무실 크기 입력
    n, m = map(int, input().split())  
    
    # 각 CCTV 종류별 감시 방향 설정
    cctv_directions = {
        1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
        2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
        3: [[(0, 1), (1, 0)], [(0, 1), (-1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]],
        4: [[(0, 1), (1, 0), (-1, 0)], [(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)], [(1, 0), (-1, 0), (0, -1)]],
        5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]],
    }
    
    office = []  # 사무실 정보
    cctvs = []  # CCTV 정보 저장

    # 사무실 정보 및 CCTV 위치와 종류 입력
    for i in range(n):
        row = list(map(int, input().split()))
        office.append(row)
        for j in range(m):
            if 1 <= row[j] <= 5:
                cctvs.append((i, j, row[j]))

    # 처음부터 모든 CCTV 방향 설정을 시작하여 최소 미감시 영역의 크기를 출력
    print(dfs(0, office, cctvs, cctv_directions))

solve()