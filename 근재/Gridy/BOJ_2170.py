# 매우 큰 도화지에 자를 대고 선을 그으려고 함
# 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다.

# 겹쳐서 그릴 수도 있고, 여러 번 그은 곳과 한 번 그은 곳은 구별 x
# 그러진 선들의 총 길이를 구하는 프로그램
import sys

input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()
# 맨 앞에서 부터 탐색 시작
start, end = arr[0][0] , arr[0][1]
result = 0
for i in range(1,N):
    print("start:", start)
    print("end: ", end)
    # 겹치는 경우
    if arr[i][0] < end < arr[i][1]:
        end = max(end,arr[i][1])
        print("endㄴ: ", end)

    # 겹치지 않는 경우
    elif arr[i][0] > end :
        result += end - start
        start = arr[i][0]
        end = arr[i][1]
        print("result: ",result)


result += end - start
print(result)
