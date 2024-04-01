## 문제 ##
# N * N 모양의 체스 판에, N 개의 퀸을 서로 공격할 수 없는 위치에 배치하는 방법의 개수를 찾는 문제
# 퀸은 상,하,좌,우,대각선 위치를 움직일 수 있다

# 2차원 배열로 풀면 시간초과 발생하므로 1차원 배열로 풀기 : 인덱스는 행으로, 값은 열로 생각
# 대각선이 가진 특성 : 서로 같은 대각선에 있다면 해당 퀸들의 행의 차이와 열의 차이가 같다

n = int(input())
answer = 0

def dfs(x, trace):  # x는 현재 행
    global answer
    if len(trace) == n: # n개의 퀸이 서로 공격하지 않고 놓일 수 있다면 answer+1
        answer += 1
        return

    for y in range(n):
        check = True
        for row, col in trace:
            # 같은 열에 퀸이 있는 경우 제외
            if y == col:
                check = False
                break
            # 대각선에 퀸이 있는 경우 제외
            if abs(x-row) == abs(y-col):
                check = False
                break

        if check:
            trace.append((x, y)) # 퀸에게 공격 받지 않는 위치인 경우 방문 처리
            dfs(x+1, trace) # 다음 행으로 옮긴 뒤 다시 탐색
            trace.pop() # 방문 끝나서 제거


dfs(0, [])
print(answer)