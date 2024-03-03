'''
말의 이동방법은 L자, 장애물을 뛰어넘을 수 있음
원숭이는 말이 되고 싶어함. 
원숭이는 K번만 말의 이동방식, 그 이후는 인접한 칸으로 이동가능(상하좌우)
말의 이동방식, 인접한 이동방식 각 1번의 움직임
최소한의 동작으로 시작점에서 도착점까지 갈 수 있는 방법을 알아내기

-- 입력
첫째줄에 정수 K ( 0 <= K 30 ), 둘째줄에 가로길이 W, 세로길이 H ( 1 <= (W, H) <= 200 ), 셋째줄이후 W x H 격자(0은 평지, 1은 장애물)

-- 출력
첫째줄에 원숭이의 동작수의 최솟값 출력, 갈수 없는 경우 -1
'''
from collections import deque
import sys

# 말 움직임과 원숭이 움직임 정의
HORSE_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
MONKEY_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 움직임 가능한 방향 반환
def get_moves(k):
    return HORSE_MOVES + MONKEY_MOVES if k > 0 else MONKEY_MOVES

# 그리드 상에서 움직일 수 있는 유효한 위치인지 체크
def is_valid_position(x, y, w, h, grid):
    return 0 <= x < w and 0 <= y < h and grid[y][x] == 0

# 최소 이동 횟수 계산 함수
def min_moves(k, w, h, grid):
    queue = deque([(0, 0, k, 0)])  # (x, y, 남은 k, 이동 횟수)
    visited = set([(0, 0, k)])

    while queue:
        x, y, k, moves = queue.popleft()

        # 목표 지점에 도달한 경우
        if x == w - 1 and y == h - 1:
            return moves

        for dx, dy in get_moves(k):
            nx, ny = x + dx, y + dy
            nk = k - 1 if (dx, dy) in HORSE_MOVES else k

            if is_valid_position(nx, ny, w, h, grid) and (nx, ny, nk) not in visited:
                visited.add((nx, ny, nk))
                queue.append((nx, ny, nk, moves + 1))

    return -1  # 목적지에 도달할 수 없는 경우

def main():
    K = int(sys.stdin.readline().strip())   # K번만 말의 움직임 가능

    # 격자 크기(가로W, 세로H), 그리고 격자 내용
    W, H = map(int, sys.stdin.readline().strip().split())                           
    grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]
    
    result = min_moves(K, W, H, grid)
    sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main()