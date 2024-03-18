# N이 150만까지이므로 O(N)이나 O(NlogN)의 복잡도를 가진 알고리즘을 생각

# < 풀이 >
# 1. 각 날짜의 최대 수익을 저장할 dp배열 생성
# 2. 1일차부터 순차적으로 이전에 저장된 최고 수익과 현재 저장된 수익 비교
# 3. 동시에 상담 종료일의 최댓값도 갱신
# 4. 최대 수익 출력

import sys

n = int(input())
arr = []
dp = [0]*(n+1) # 마지막 날까지 최대로 받을수 있는 금액을 표시해줄 리스트

for _ in range(n):
	arr.append(list(map(int, sys.stdin.readline().split())))

maximum = 0 # 각 날짜별로 최대 얼마를 벌어왔는지 확인할 변수 생성
for i in range(n):
	maximum = max(maximum, dp[i]) # 현재 날짜에 저장된 번 돈을 "이전" 최대 금액과 비교하여 큰 값 선택
	next_location = i + arr[i][0] # 일이 끝나는 날을 지정
	if next_location <= n: # 퇴사 전에 일이 끝나는 경우
		# (이전에 번 최대 금액 + 일이 끝나면 받을 돈)과 (일이 끝나는 날에 저장되어있던 최대 금액) 비교하여 큰 값을 선택
		dp[next_location] = max(maximum + arr[i][1], dp[next_location])

print(max(dp))