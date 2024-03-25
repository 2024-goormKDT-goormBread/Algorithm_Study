# 여러 개의 정사각형 칸들로 이루어진 정사각형 모양의 종이가 주어져 있고,
# 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있음.

# 전체 종이의 크기가 N*N이라면 종이를 자르는 규칙은
# 1. 모두 같은 색이 아니라면 가로와 세로로 중간을 자른다.
# 2. N/2xN/2 색종이 네개로 나눈 것을 마찬가지로 방법 1을 반복한다.
# 3. 종이가 모두 하얀색 or 파란색으로 칠해져있거나, 하나의 정사각형 칸이
# 되어 더 이상 자를 수 없을 때까지 반복

# 하얀색 종이와 파란색종이의 개수를 구하는 프로그램 작성
# 0은 하얀색, 1은 파란색
import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

def colorpaper(r, c, n):
    num = paper[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != num:
                colorpaper(r, c, n // 2)
                colorpaper(r, c + n // 2, n // 2)
                colorpaper(r + n // 2, c, n // 2)
                colorpaper(r + n // 2, c + n // 2, n // 2)
                return

    if num == 0:
        answer[0] += 1
    else:
        answer[1] += 1


colorpaper(0, 0, N)
print(*answer, sep='\n')
