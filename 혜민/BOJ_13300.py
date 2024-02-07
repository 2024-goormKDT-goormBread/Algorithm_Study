from bisect import bisect_right, bisect_left

def count_0_1(a,right,left):
	right_index = bisect_right(a,right)
	left_index = bisect_left(a,left)
	return right_index-left_index

n, k = map(int, input().split())

graph=[[] for _ in range(7)]

#간선정보 입력 받기 
for _ in range(n):
	s, y = map(int, input().split())
	graph[y].append(s)

count = 0 
for i in range(1,7):
	graph[i].sort()
	index_0 = count_0_1(graph[i],0,0)
	index_1 = count_0_1(graph[i],1,1)
	if index_0%k == 0:
		count+=(index_0//k)
	else:
		count+=(index_0//k+1)
	if index_1%k == 0:
		count+=(index_1//k)
	else:
		count+=(index_1//k+1)

print(count)
