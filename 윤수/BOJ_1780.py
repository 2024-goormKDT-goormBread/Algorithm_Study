'''
문제제목: 종이의 개수(http://acmicpc.net/problem/1780)
문제요약:
    N*N 크기의 종이가 주어졌을 때, 종이를 9등분하여 각 종이의 숫자가 같은지 확인하는 문제
    만약 종이의 숫자가 모두 같다면, 종이의 숫자를 출력하고 아니라면 9등분하여 확인  
풀이방법: 
    1. 종이의 숫자가 모두 같은지 확인하는 함수를 만들어서 모두 같다면 해당 숫자를 반환
    2. 모두 같지 않다면, 9등분하여 각각의 종이를 확인
    3. 9등분한 종이의 숫자를 확인하여 모두 같다면 해당 숫자를 반환
    4. 9등분한 종이의 숫자를 확인하여 모두 같지 않다면, 9등분한 종이의 숫자를 반환  

'''

def is_uniform(x, y, size):
    initial = MATRIX[x][y]
    
    for i in range(x, x + size):      # 
        for j in range(y, y + size):
            if MATRIX[i][j] != initial:  # 요소가 모두 다른지 비교
                return False
    return True

def count_numbers(x, y, size):
    # 모두 같은 요소인지 확인하고 카운트
    if is_uniform(x, y, size):
        COUNTS[MATRIX[x][y] + 1] += 1  # +1을 하는 이유는 인덱스( 0, 1, 2)와 숫자(-1, 0, 1)를 맞추기 위함
        return
    
    # 다른 요소가 있다면 9등분하여 각각의 종이를 확인
    sub_size = size // 3
    for dx in range(3):
        for dy in range(3):
            count_numbers(x + dx * sub_size, y + dy * sub_size, sub_size)

N = int(input())
MATRIX = [list(map(int, input().split())) for _ in range(N)]
COUNTS = [0, 0, 0]  # -1, 0, 1에 대한 카운트 초기화

count_numbers(0, 0, N)

# -1, 0, 1에 대한 최종 카운트 출력
for count in COUNTS:
    print(count)