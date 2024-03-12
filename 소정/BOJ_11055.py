# < 문제 >
# 가장 긴 부분 수열의 합을 구하는 문제
# 예시)
# 1 100 2 50 60 3 5 6 7 8의 경우
# 1 101 3 53 113 6 11 17 24 32가 나와야 한다

# < 풀이 >
# 만약 arr[i] > arr[j]라면, dp[i]와 dp[j] + arr[i] 중 큰 값을 dp[i]로 갱신
# 만약 arr[i] <= arr[j]라면, 기존의 dp[i]와 arr[i] 중 큰 값으로 갱신

# arr[i] <= arr[j]를 고려하는 이유
# 뒤의 과정의 수행을 위해 현재값(arr[i])부터 시작하는 부분 수열을 고려해주어야 한다
# 예시)
# 10 20 10 30 20 50의 경우,
# 10 30 10 60 30 110이 나와야 하는데
# arr[i] <= arr[j]를 고려안하면
# 10 30 0 60 30 110이 나온다

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = arr[0]

for i in range(1,n):
	for j in range(i):
		# 만약 arr[i] > arr[j]라면, dp[i]와 dp[j] + arr[i] 중 큰 값을 dp[i]로 갱신
		if arr[i] > arr[j]:
			dp[i] = max(dp[i], arr[i] + dp[j])
		# 만약 arr[i] <= arr[j]라면, 기존의 dp[i]와 arr[i] 중 큰 값으로 갱신
		else:
			dp[i] = max(dp[i], arr[i])
	
print(max(dp))