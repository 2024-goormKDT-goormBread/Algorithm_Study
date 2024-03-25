'''
문제제목: 쿼드트리(http://acmicpc.net/problem/1992)
문제요약:
    N*N 크기의 영상이 주어졌을 때, 이를 압축하는 문제
    만약 영상이 모두 0이라면, 0을 출력하고 모두 1이라면 1을 출력
    그렇지 않다면, 4등분하여 각각의 영상을 확인 
풀이방법:
    1. 영상이 모두 같은지 확인하는 함수를 만들어서 모두 같다면 해당 숫자를 반환
    2. 모두 같지 않다면, 4등분하여 각각의 영상을 확인
    3. 4등분한 영상의 숫자를 확인하여 모두 같다면 해당 숫자를 반환
    4. 4등분한 영상의 숫자를 확인하여 모두 같지 않다면, 4등분한 영상의 숫자를 반환  
'''

def compress(x, y, size):
    uniform = True
    initial = MATRIX[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 하나라도 다른 요소가 있는지 검사
            if MATRIX[i][j] != initial:
                uniform = False
                break
        if not uniform:
            break
    
    if uniform: # 영역이 균일하면 해당 숫자 반환
        return str(initial)
    else:       # 균일하지 않으면 영역을 4등분
        sub_size = size // 2
        
        top_left = compress(x, y, sub_size)
        top_right = compress(x, y + sub_size, sub_size)
        bottom_left = compress(x + sub_size, y, sub_size)
        bottom_right = compress(x + sub_size, y + sub_size, sub_size)
        
        return '(' + top_left + top_right + bottom_left + bottom_right + ')'

N = int(input())
MATRIX = [list(map(int, input())) for _ in range(N)]
print(compress(0, 0, N))
