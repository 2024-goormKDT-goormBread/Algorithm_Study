# 1~6학년들이 묵을 방을 배정 성별끼리 방 배정
# 한 방에는 같은 학년의 학생들 배정
# 한 방에 한 명만 배정하는 것도 가능
# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때,
# 조건에 맞게 모든 학생들을 배정하기 위해 필요한 방의 최소 개수

# 성별 S와 학년으로 분리 여학생은 0, 남학생은 1

N, K = map(int, input().split())
students = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
result = 0
for i in range(N):
    S, grade = map(int, input().split())
    students[S][grade - 1] += 1

for i in students:
    for j in i:
        if j % K == 0:
            result += (j // K)
        else:
            result += (j // K) + 1
print(result)
