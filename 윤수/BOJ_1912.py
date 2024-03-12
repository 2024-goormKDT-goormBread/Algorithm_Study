'''
연속합 문제: https://www.acmicpc.net/problem/1912
문제 요약: 
    n개의 정수로 이루어진 임의의 수열이 주어진다. 이때 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하는 문제
    단, 수는 한 개 이상 선택해야 한다.
'''
n = int(input())  # 수열의 길이 입력 받기
arr = list(map(int, input().split()))  # 수열 입력 받기

# DP 테이블 초기화
dp = [0] * n
dp[0] = arr[0]  # 첫 번째 원소는 자기 자신이 최대값

# DP 테이블 갱신
for i in range(1, n):
    # 이전까지의 연속합과 현재 수를 더한 값과 현재 수 중 큰 값을 선택
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

# 최대 연속합 출력
print(max(dp))