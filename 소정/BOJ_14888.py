import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr_num = list(map(int, sys.stdin.readline().split()))
add, sub, multi, div = map(int, sys.stdin.readline().split())
operator = ['+']*add + ['-']*sub + ['*']*multi + ['//']*div
max_result = -1000000000
min_result = 1000000000

# operator = []
# for oper in permutations(operator, n-1):
# 	if oper not in arr_operator:
# 		arr_operator.append(oper)
# 이렇게 하면 시간 초과 발생 
# 왜? permutations 할 때 set을 이용해 미리 중복을 제거하지 않으면 반복문 헛도는게 많아지기 때문이다.

for oper in set(permutations(operator, n-1)): 
	value = arr_num[0]
	for i in range(n-1):
		if oper[i] == '+':
			value += arr_num[i+1]
		elif oper[i] == '-':
			value -= arr_num[i+1]
		elif oper[i] == '*':
			value *= arr_num[i+1]
		else:
			if value < 0:
				value =  -(abs(value)//arr_num[i+1])
			else:
				value //= arr_num[i+1]

	if value < min_result:
		min_result = value
	if value > max_result:
		max_result = value

print(max_result)
print(min_result)