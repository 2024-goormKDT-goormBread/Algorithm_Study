'''
문제제목: N과 M(12) (http://acmicpc.net/problem/15666)
문제요약:
    1부터 N까지 자연수 중에서 M개를 고른 수열을 모두 구하는 문제
    단, 같은 수를 여러 번 골라도 된다.
    고른 수열은 비내림차순이어야 한다.
풀이방법:
    1. 중복조합을 구하는 문제이므로, 중복조합을 구하는 함수를 구현
    2. 중복조합을 구하는 함수를 호출하여 결과를 출력
'''
from itertools import combinations_with_replacement

# itertools 표준 라이브러리를 사용한 풀이
def use_itertools(numbers, M):
    for combination in sorted(set(combinations_with_replacement(numbers, M))): # set을 쓴 이유는 중복되는 수열을 여러번 출력하면 안되기 때문
        print(' '.join(map(str, combination)))

# 백트래킹을 사용한 풀이    
def use_backtracking(numbers, M, result, depth, start):
    # M은 생성하려는 조합의 개수, depth는 현재까지 생성한 조합의 개수(재휘호출 깊이)
    if depth == M: 
        print(' '.join(map(str, result)))
        return
    
    prev_num = 0
    for i in range(start, len(numbers)): 
        if prev_num != numbers[i]:       # 이전 숫자와 현재 숫자가 같지 않다면
            result.append(numbers[i])    # 결과 리스트(스택)에 추가
            use_backtracking(numbers, M, result, depth + 1, i) # 재귀함수 호출
            result.pop()                 # 이전 상태로 돌아가기 위해 Pop
            prev_num = numbers[i]

def solve():
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))

    use_itertools(numbers, M)
    use_backtracking(numbers, M, [], 0, 0)

solve()