# combination 함수 사용 시
# 서로 다른 숫자중 n개를 선택 할 때 순서를 고려하지 않고 중복없이 뽑을 경우의 수 튜플로 반환
from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break

    n = arr[0]
    arr = arr[1:]
    for comb in combinations(arr, 6): 
      print(*comb)
    print()