from sys import stdin

# 1. 입력받기
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, stdin.readline().split())))

# 종이 종류별로 저장하기 위해 딕셔너리 자료형 사용
result = {-1:0, 0:0, 1:0}

# 2. 종이의 종류(-1, 0, 1)와 다르면 분할 
def divided(x, y, n):
	for i in range(x, x+n):
		for j in range(y, y+n):
			# 현재 종이 종류와 다르다면 
			if graph[x][y] != graph[i][j]:
				# 종이 1/3로 분할
				length = n//3
				# 종이를 같은 크기의 종이 9개로 자르므로 
				divided(x, y, length)
				divided(x, y+length, length)
				divided(x, y+(length*2), length)
				divided(x+length, y, length)
				divided(x+length, y+length, length)
				divided(x+length, y+(length*2), length)
				divided(x+(length*2), y, length)
				divided(x+(length*2), y+(length), length)
				divided(x+(length*2), y+(length*2), length)
				return
			
	# 3. 종이 종류에 따라 count 
	result[graph[x][y]] +=1 
	return 

divided(0,0,n)

# 4. 결과 return 
for i in result.values():
    print(i)

