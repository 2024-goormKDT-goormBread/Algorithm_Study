n=int(input())

#맵 정보 입력
graph = [list(map(int,input().split())) for _ in range(n)]

#1,0,-1에 대한 결과를 담을 변수 선언
result1=0
result0=0
result_1=0


def search(x,y,n):
    global result_1, result0, result1
    start = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != start:    #값이 동일하지 않은것이 발견되면 3분할 실행 
                for a in range(3):
                    for b in range(3):
                        search(x+a*n//3, y+b*n//3, n//3)
                return
    
    #해당하는 값에 1씩 카운팅
    result_1 += 1 if start == -1 else 0 
    result0 += 1 if start == 0 else 0
    result1 += 1 if start == 1 else 0


search(0,0,n)
print(result_1)
print(result0)
print(result1)
