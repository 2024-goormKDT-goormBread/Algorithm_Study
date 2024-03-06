# 인하은행에 ATM이 1개만 있고 N명이 1~N번까지 줄을 서있음.
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분

# 사람들이 줄서는 순서에 따라 돈을 인출하는 필요한 시간의 합이 달라진다.
# 예를 들어  P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우
# [1,2,3,4,5] 순서로 줄을 선다면,
# 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분

# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성

# 한 마디로 돈을 뽑을 때 적게 걸리는 사람이 가장 앞에 와야한다.

N = int(input())
person = list(map(int, input().split()))
result = []
S = 0
person = sorted(person)
for i in range(len(person)):
    S += person[i]
    result.append(S)
print(sum(result))