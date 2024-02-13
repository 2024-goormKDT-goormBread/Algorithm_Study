# 돈을 잘못 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킴
# 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶다.
K = int(input())
# 값들을 저장할 Array
arr = []

for i in range(K):
    # 정수 입력
    N = int(input())
    # 0을 만나면 맨 위의 인덱스값 pop
    if N == 0:
        arr.pop()
    else:
    # 아닌 경우에는 값을 저장
        arr.append(N)

print(sum(arr))