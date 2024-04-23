import sys
from itertools import combinations, permutations

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
number = [i for i in range(n)]
gap = 10000

for team_A in combinations(number, n//2):
	team_B = set(number) - set(team_A)

	A_value = 0
	B_value = 0
	for A_1, A_2 in permutations(team_A, 2):
		A_value += arr[A_1][A_2]
	for B_1, B_2 in permutations(team_B, 2):
		B_value += arr[B_1][B_2]
	if gap > abs(A_value - B_value):
		gap = abs(A_value - B_value)

print(gap)