# N = 6이면 > N이 3일 때의 삼각형 3개로 분할이 가능하고
# N = 12이면 N이 6일 때의 삼각형 3개로 분할이 가능
# N = 24 N이 12일때의 삼각형 3개로 분할이 가능
import sys

input = sys.stdin.readline

n = int(input())
# 전체 배열 생성
stars = [[' '] * 2 * n for _ in range(n)]


def recursion(i, j, size):
    # N이 3이 되었을 때
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    # 아닌 경우라면 3이 될 때까지 분할한다.
    else:
        newSize = size // 2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)


# 함수 호출
recursion(0, n - 1, n)
for star in stars:
    print("".join(star))
