'''
문제제목: 쉬운 계단 수(www.acmicpc.net/problem/10844)
문제요약:
    0~9까지의 숫자로 이루어진 계단 수가 있다. 이때 인접한 수가 1차이 나는 수를 계단수라고 한다.
    길이가 N인 계단수의 개수를 구하는 문제.
    0으로 시작하는 수는 없다.
'''
n = int(input())  # 계단 수의 길이 입력 받기

# DP 테이블 초기화
dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1인 경우 초기값 설정
for i in range(1, 10):
    dp[1][i] = 1

# DP 테이블 갱신
for i in range(2, n + 1):
    for j in range(10):
        # 0과 9는 특별한 경우로 처리
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 결과 계산
result = sum(dp[n]) % 1000000000
print(result)