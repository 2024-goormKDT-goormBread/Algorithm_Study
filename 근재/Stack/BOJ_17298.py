# 크기가 N인 수열 A = A1,...AN이 있다. 수열의 원소 Ai에 대해서 오큰수 NEG(i)를 구하려고 함
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미.
# 그러한 수가 없는 경우에 오큰수는 -1임.

# 예를 들어, A = [3,5,2,7]인 경우 NGE(1)=5,NGE(2)=7,NGE(3)=7,NGE(4)=-1이다.
# A = [9,5,4,8]이면 NGE(1)=-1,NGE(2)=8,NGE(3)=8,NGE(4)=-1

N = int(input())
A = list(map(int,input().split()))
stack = []

answer = [-1]*N

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)
