############# < 문제 > #############
# < 쇠막대기와 레이저의 배치 조건 >
# 1. 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. 
# -> 완전히 포함되도록, 끝점은 겹치지 않도록
# 2. 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 3. 레이저는 쇠막대기의 끝점과 겹치지 않는다.

# < 레이저와 쇠막대기의 배치 표현 >
# 1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( )’ 으로 표현
# 2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현

############# < 풀이 > #############
# 1. '('를 만났을 때, 
# -> flag = 0
# -> queue에 append (= 끝을 모르는 쇠막대기 추가)
#
# 2. ')'를 만났을 때,
# 2-1. '(' 이후에 바로 ')'이 나온 경우 = 레이저인 경우
# -> flag = 1
# -> queue로부터 pop (= 레이저 생성)
# -> 만들어진 레이저는 queue에 들어있는 쇠막대기들을 각각 자르므로 count += len(queue)
# 2-2. ')'이 연달아 나온 경우 = 쇠막대기의 끝점인 경우
# -> flag 값이 여전히 1인 상태
# -> queue로부터 pop (= 끝점이 생긴 쇠막대기 제거)
# -> 제거된 쇠막대기의 마지막 부분이 잘려나갔으므로 count += 1

import sys
from collections import deque

sign = list(sys.stdin.readline().rstrip())
queue = deque()
flag = 0
count = 0

for i in sign:
	if i == '(' :
		flag = 0
		queue.append(i)
	elif i == ')':
		if flag == 0:
			flag = 1
			queue.pop()
			count += len(queue)
		elif flag == 1:
			queue.pop()
			count += 1

print(count)



