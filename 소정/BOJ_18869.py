## 문제 ##
# M개의 우주가 있고, 각 우주에는 1부터 N까지 번호가 매겨진 행성이 N개 존재
# 행성의 크기를 알고 있을때, 균등한 우주의 쌍이 몇 개인지 구하기
# 균등한 쌍이란?
# Ai < Aj → Bi < Bj
# Ai = Aj → Bi = Bj
# Ai > Aj → Bi > Bj

## 풀이 ##
# 우주의 행성을 크기 순서대로 순위를 매겼을 때, 
# 행성의 순위 순서가 동일한 다른 우주가 있다면
# 두 우주는 균등한 우주의 쌍이라 한다

import sys
from itertools import combinations

m, n = map(int, input().split())
rank = []
for _ in range(m):
	arr = list(map(int, sys.stdin.readline().split())) 
	arr_sort = sorted(list(set(arr))) # 크기가 같은 행성의 순위는 동일하므로 중복 삭제
	index = {arr_sort[i] : i for i in range(len(arr_sort))} 
	rank.append(tuple([index[i] for i in arr])) # 문제에서 주어진 우주의 행성 순서에 따른 크기 순위 리스트

count = 0
for i in combinations(rank, 2): 
	if i[0] == i[1]: # 행성의 크기 순서가 같은 우주의 쌍 
		count += 1
print(count)