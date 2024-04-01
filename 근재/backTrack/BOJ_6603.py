# 독일 로또 {1,2,..., 49}
# 49가지 중 k(k>6)개의 수를 골라 집합 S를 만든 다음
# 그 수만 가지고 번호를 선택하는 것

# 예를 들어 k=8, S={1,2,3,5,8,13,21,34}이면
# 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지
# 집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램

def backTrack(arr, s, index, cnt):
    if cnt == 6:
        print(*arr)
        return

    for i in range(index, len(s)):
        arr[cnt] = s[i]
        backTrack(arr, s, i + 1, cnt + 1)


while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break

    arr = [0] * 6
    backTrack(arr, S[1:], 0, 0)
    print()
