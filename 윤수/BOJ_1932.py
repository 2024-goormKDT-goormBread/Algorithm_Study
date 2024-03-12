'''
정수삼각형 문제: https://www.acmicpc.net/problem/1932
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하라.
아래 층에 있는 수는 현재 층에서 선택된 수의 댁각선 왼쪽, 대각선 오늘쪽에 있는 것중에서만 선택 가능

'''
n = int(input())  # 정수 삼각형의 크기 입력 받기

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))  # 삼각형 입력 받기

# 삼각형의 각 위치까지의 최대 합을 저장할 DP 테이블 초기화
dp = [[0] * i for i in range(1, n + 1)]

# DP 테이블 갱신
dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        # 맨 왼쪽 끝에 있는 경우
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        # 맨 오른쪽 끝에 있는 경우
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        # 가운데에 있는 경우
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

# 최대값 출력
print(max(dp[n - 1]))