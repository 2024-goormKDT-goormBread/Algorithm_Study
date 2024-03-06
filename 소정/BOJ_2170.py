# < 문제 >
# 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성
# 선이 여러 번 그려진 곳은 한 번씩만 계산

# < 풀이 >
# 왼쪽의 위치부터 차례대로 선을 그어가기 위해 입력을 받은 후 정렬
#
# 시작점과 도착점을 각각 start, end라 했을 때 세 가지 경우가 존재할 수 있음
# 1. 두 선이 겹치고 그 때 꺼낸 도착점이 end보다 뒤에 있는 경우,
# end를 새로운 도착점으로 갱신
# 2. 두 선이 겹치고 그 때 꺼낸 도착점이 end보다 앞에 있는 경우, 무시
# 3. 두 선이 겹치지 않는 경우, 
# start, end와 겹치는 선은 없으므로, 그 길이를 계산하여 결과값(sum)에 더한다. 
# start, end를 새로운 시작점과 도착점으로 갱신


import sys

n = int(input())
list = []
for i in range(n):
	x, y = map(int, sys.stdin.readline().split())
	list.append([x,y])

list.sort(key = lambda x: (x[0], -x[1]))
start, end = list[0][0], list[0][1]
sum = 0

for i in range(1,n):
	if start <= list[i][0] <= end:
		if end < list[i][1]:
			end = list[i][1]
	else:
		sum += end - start
		start, end = list[i][0], list[i][1]

sum += end - start
print(sum)