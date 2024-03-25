# n * n 크기의 행렬로 표현되는 종이가 있음
# 종이의 각 칸에는 -1,0,1 중 하나가 저장되어 있음.
# 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자른다.


# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용
# 1이 아닌 경우에 종이를 같은 크기의 종이 9개로 자르고, 각각의
# 잘린 종이에 대해서 (1)의 과정을 반복한다.

# 이와 같이 종이를 잘랐을 때 -1 로만 채워진 종이의 개수, 0으로만
# 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그
# 램을 작성
import sys

input = sys.stdin.readline


def cut_paper(r, c, n):
    num = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        cut_paper(r + k * (n // 3), c + l * (n // 3), n // 3)
                return

    if num == -1:
        ans[0] += 1
    elif num == 0:
        ans[1] += 1
    else:
        ans[2] += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

cut_paper(0, 0, n)
print(*ans, sep='\n')
