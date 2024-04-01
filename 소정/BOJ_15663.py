## 문제 ##
# 순열을 중복없이 출력하는 문제

## 풀이 ##
# 각 자리의 방문을 체크하고, 이미 방문한 원소 다시 쓰지 않게 처리
# set을 사용하여 중복 제거하고 출력

import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [0]*n # 방문 여부
s = [] 
result = []

def dfs():
	if len(s) == m:
		result.append(list(s)) # 정답 리스트에 추가
		return
	
	for i in range(n):
		if visited[i] == 0:
			s.append(arr[i])
			visited[i] = 1 # 방문 처리
			dfs()
			s.pop()
			visited[i] = 0 # 방문 해제

dfs()

result = sorted(list(set([tuple(i) for i in result]))) # 중복 제거 및 정렬
for i in range(len(result)):
	print(*result[i]) 

