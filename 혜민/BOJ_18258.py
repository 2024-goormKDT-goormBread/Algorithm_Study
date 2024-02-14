from collections import deque
import sys

queue = deque()
n = int(input())

for _ in range(n):
	x = sys.stdin.readline().split()    #많은 양의 데이터를 받아야해서 sys.stdin으로 input 받기
	if x[0] == 'push':
		queue.append(x[1])
	elif x[0] == 'pop':
		if queue:              #큐가 True이면 = 큐가 비어있지 않다면 
			print(queue.popleft())
		else:                   #큐가 False라면 = 큐가 비어있다면
			print('-1')
	elif x[0] == 'size':
		print(len(queue))
	elif x[0] == 'empty':
		if queue:
			print('1')
		else:
			print('0')
	elif x[0] == 'front':
		if queue:
			print(queue[0])
		else:
			print('-1')
	elif x[0] == 'back':
		if queue:
			print(queue[-1])
		else:
			print('-1')
			