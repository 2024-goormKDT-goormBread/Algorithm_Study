# n개의 원반을 특정 기둥으로 옮기려면, 
# 1. 맨 아래를 제외한 원반들을 다른 기둥으로 옮기고
# 2. 맨 아래 원반을 목적지 기둥으로 옮기고 
# 3. 다른 기둥에 옮겼던 원반들을 그 위에 얹는것
# 이러한 과정이 반복된다

# 원반갯수, 출발지 기둥위치, 목적지 기둥위치, 나머지 기둥위치
def hanoi(num, from_, to, other):
	if num == 0:
		return 
	# 받아온 원반 갯수보다 하나적은 원반들을 목적지가 아닌 곳으로 이동
	hanoi(num-1, from_, other, to) 
	# 마지막 원반을 목적지로 이동
	disk.append([from_, to])
	# 다른 곳으로 옮겼던 원반들을 그 위에 얹는다
	hanoi(num-1, other, to, from_)

n = int(input())
disk = []

hanoi(n, 1, 3, 2)

# 옮긴 횟수 출력
print(len(disk))
# 옮기기 전과 후 위치 출력
for i in range(len(disk)):
	print(disk[i][0], disk[i][1])