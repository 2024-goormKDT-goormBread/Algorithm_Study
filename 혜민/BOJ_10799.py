#괄호 입력
array = list(input())

stack = []
count = 0
for x in array:   #입력리스트에 있는 괄호를 하나씩 확인 
    if x == "(":    
        stack.append(x)  #x가 왼쪽 괄호면 스택에 append
        before_x = x     #이전의 x값과 항상 비교해야하니까 before_x 변수에 현재 변수값 업데이트
    else:              
        if x == before_x:    #x가 오른쪽 괄호이고 이전과 같다면, 끝조각용이므로
            stack.pop()      #pop하고, 남은 끝조각 count +1
            count+=1
            before_x = x
        else:                #이전과 다르다면, 레이저용이므로 
            stack.pop()
            count+=len(stack)  #pop하고, count +현재 스택의 사이즈 
            before_x = x   
            
print(count)
