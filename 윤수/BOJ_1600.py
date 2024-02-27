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
# | 구분 | 원숭이 | 말 |
# |:---:|:---:|:---:|
# |이동|상하좌우 인접|L자 모양|
# |장애물|불가|가능|
# 
import sys
from collections import deque

class Directions:
    HORSE_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    MONKEY_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 미친 원숭이(말이 되고픈 원숭이) 클래스 정의
class CrazyMonkey:
    def __init__(self, horse_moves_count):
        self.horse_moves_count = horse_moves_count
    
    # 움직임 가능한 방향 결정
    def available_moves(self):
        if self.horse_moves_count > 0:
            return Directions.HORSE_MOVES + Directions.MONKEY_MOVES
        return Directions.MONKEY_MOVES

    # 현재 위치에서 특정거리(distance) 만큼 움직임
    def move(self, position, distance, is_horse_move): # position: (x,y), distance: (dx, dy), is_horse_move: bool
        # 말처럼 움직인다면 count 1 감소
        if is_horse_move and self.horse_moves_count > 0:
            self.horse_moves_count -= 1
        return (position[0] + distance[0], position[1] + distance[1])

# 그리드 상에서 움직일 수 있는 유효한 위치인지 체크
def is_valid_position(position, width, height, grid):
    # 위치가 gird 내에 있어야하고, 평지(0)야한다.
    return (0 <= position[0] < width) and (0 <= position[1] < height) and (grid[position[1]][position[0]] == 0)


def count_moves_monkey(K, W, H, grid):  # BFS 활용
    monkey = CrazyMonkey(K)             # 말이 되고 싶은 원숭이 객체 생성
    start_position = (0, 0)             # 시작 위치
    initial_count = 0                   # 초기 이동 횟수
    initial_state = (start_position, initial_count, monkey)

    queue = deque([initial_state])
    visited = set([(0, 0, K)])          # 위치값과 K값을 방문시 저장

    while queue: 
        (current, count, monkey) = queue.popleft()         # 현재 위치, 이동 횟수, 원숭이 객체 추출

        if current[0] == W - 1 and current[1] == H - 1:    # 목표지점 도달
            return count

        for move in monkey.available_moves():                # 원숭이의 모든 움직임에 대해서 반복
            # 현재 위치에서 원숭이냐 말이냐에 따라 거리만큼 움직이고 새로운 위치값 반환
            new_position = monkey.move(current, move, move in Directions.HORSE_MOVES)
            
            # 새 위치가 유효하고, 아직 방문하지 않은 위치인 경우
            if is_valid_position(new_position, W, H, grid) and (new_position[0], new_position[1], monkey.horse_moves_count) not in visited:
                # 새 위치를 방문한 것으로 표시하고 큐에 저장
                visited.add((new_position[0], new_position[1], monkey.horse_moves_count))  
                queue.append((new_position, count + 1, monkey))

    return -1  # 목표 지점에 도달할 수 없는 경우 -1 반환

def main():
    K = int(sys.stdin.readline().strip())   # K번만 말의 움직임 가능

    # 격자 크기(가로W, 세로H), 그리고 격자 내용
    W, H = map(int, sys.stdin.readline().strip().split())                           
    grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]
   
    result = count_moves_monkey(K, W, H, grid)
    sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main()