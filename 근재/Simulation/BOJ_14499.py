# NxM 지도에 주사위 하나가 있음
# 지도의 좌표는 r,c로 나타낸다
# 주사위는 지도 윗 면이 1이고, 동쪽 바라보는 방향이 3인
# 상태로 놓여져 있고, 놓인 곳 좌표는 x,y이다. 처음 주사위는 0으로 되어있음

# 지도의 각 칸에는 정수가 하나씩 쓰여져 있음.
# 이동한 칸이 0이면 주사위에 수가 복사 0이 아니면 칸의 수가 주사위 바닥면으로 복사
# 칸에 있는 수는 0이 됌

# 동서북남 1 2 3 4
# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때,
# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성

def roll(move):
    if move == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[
            2]  # 주사위 변화 4 2 1 6 5 3
    elif move == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[
            3]  # 주사위 변화 3 2 6 1 5 4
    elif move == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[
            1]  # 주사위 변화 5 1 3 4 6 2
    elif move == 4:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[
            4]  # 주사위 변화 2 6 3 4 1 5


n, m, x, y, k = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]
order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
# 이동 방법 인덱스를 맞춰 주었음
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for i in order:
    if 0 <= y + dy[i - 1] < n and 0 <= x + dx[i - 1] < m:  # 조건 0
        y = y + dy[i - 1]
        x = x + dx[i - 1]
        roll(i)
        # 이동한 위치가 0이라면 주사위의 수를 복사
        if arr[y][x] == 0:
            arr[y][x] = dice[5]
        # 0이 아니라면 주사위에 복사하고 위치의 숫자를 삭제
        else:
            dice[5] = arr[y][x]
            arr[y][x] = 0
        print(dice[0])
