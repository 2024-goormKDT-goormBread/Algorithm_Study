'''
여러개의 선분이 주어지고, 각 선분은 두개의 정수로 표현된다. 이 정수들은 선분의 시작점과 끝점을 나타낸다.
이 선분들이 서로 겹치거나 접할 수 있으며, 이 경우 겹치는 부분은 중복으로 계산하지 않는다.
최종적으로 모든 선분들을 합쳤을 때의 총 길이를 구한다.
'''
import sys

def totalLength(lines):
    total_length = 0
    lines.sort()
    
    start, end = lines[0]            
    for i in range(1, len(lines)):  
        if lines[i][0] <= end:           # 두 선분이 겹치는 경우
            end = max(end, lines[i][1])  # 두 선분의 끝점 중 큰값으로 갱신
        else:                            # 두 선분이 겹치지 않는 경우
            total_length += end - start  # 이전 선분의 길이를 더함
            start, end = lines[i]        # 새로운 선분으로 갱신
    total_length = total_length + (end - start)
    
    return total_length

def solve():
    N = int(sys.stdin.readline().strip())
    lines = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    print(totalLength(lines))
    
solve()