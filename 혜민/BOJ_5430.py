from collections import deque

def D_func(queue, R_count):
    if len(queue) == 0:
        return 0
    else:
        if R_count % 2 == 1:
            queue.pop()     #홀수면 오른쪽 pop
            return list(queue)
        else:
            queue.popleft()    #짝수면 왼쪽 pop
            return list(queue)

ans = []
T = int(input())
for _ in range(T):
    func = input()
    n = int(input())
    arr = list(input()[1:-1].split(',')) 
    R_count = 0

    queue = deque(arr)

    if n == 0:  #빈 배열이 들어왔을때 ['']이 상태로 인식이 되면, 길이가 0이 아닌 1로 인식되므로 빈 리스트로 초기화해줘야함
        queue = []

    for f in func:         
        if f == 'R':        #R인 경우엔 나중에 한번에 연산해야하기 떄문에 count만 하기 
            R_count += 1
        else:
            queue = D_func(queue, R_count)      #D인 경우에 D함수 호출
            if queue == 0:  
                break

    #함수 연산이 끝난 후 r_count 값에 따른 리버스 수행
    if R_count % 2 == 1:
        queue.reverse()

    #queue가 비어있다면 error 정답 리스트에 추가, 아니면 큐 추가 
    if queue == 0:
        ans.append('error')
    else:
        ans.append(queue)

for a in ans:
    if a == 'error':
        print(a)
    else:
        print("[" + ",".join(a) + "]")
