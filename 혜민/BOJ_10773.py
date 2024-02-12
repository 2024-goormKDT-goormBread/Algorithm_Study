#k입력
k = int(input())

stack = []
for _ in range(k):
	x = int(input())    #받아적을 수 입력
	if x == 0:          #만약 0이면/잘못부른것이라면
			if len(stack)==0:   #그리고 잘못 불렀는데, 만약 스택에 아무것도 없다면
				stack.append(x) #0이라도 append
			else:
				stack.pop()     #스택에 있는데 잘못 부른것이면, pop
	else:               #정상적인 경우, 해당 숫자 그냥 스택에 append
		stack.append(x)

print(sum(stack))	        #스택의 합 출력 
