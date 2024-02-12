'''
N개의 높이가 서로 다른 탑을 왼쪽부터 오른쪽방향으로 세우고, 각 탑의 꼭대기에 레이저 송신기 설치
레이저송신기는 레이저신호를 지표면과 수평으로 왼쪽 방향으로 발사, 탑의 기둥 모두에는 수신기 설치
하나의 탑에서 발사된 레이저신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능

예시로
높이6,9,5,7,4 다섯개탑이 수평으로 서있고 모든 탑에서는 주어진 탑 순서의 반대방향(왼쪽)으로 레이저를 발사
높이4인 다섯번째탑에서 발사한 레이저신호는 높이7인 네번째탑이 수신하고
높이7인 네번째탑의 신호는 높이9인 두번째탑이, 높이5인 세번째신호는 높이9인 두번째탑이 수신을 한다
높이가8인 두번째 탑과, 높이6인 첫번째탑은 수신하지 못한다.

탑들의 개수 N, 탑들의 높이가 주어질때, 각각의 탑에서 발사한 레이저신호를 어느탑에서 수신하는가

-- 입력
첫째줄에 탑의 수 N (1 <= N 500000 )
둘째줄에 N개의 탑들의 높이가 직전상에 놓인 순서대로 나열(공백 구분)
탑의 높이 H ( 1 <= H <= 100000000 )

-- 출력
각 탑이 레이저 신호를 수신한 탑번호들의 번호 출력(공백구분)
레이저신호를 수신하지 못하면 0으로 출력

'''

# + 문제상황에서 스택ADT 재정의 + 
# 0. Stack: 송신 타워 목록(수신이 확인되지 않은 타워 추적)
# 1. peek: 최근/이전에 입력된 타워
# 2. push: 새 타워(추적할 대상) 추가
# 3. pop: 수신타워가 있으면(수신타워높이가 높거나 같으면) 목록에서 제거
# 4. isEmpty: 비교할 타워가 없는지 비교

# 결론: 아래 함수는 for중첩으로 '시간초과' 발생  O(N^2)
# def ReceivedTowers(heights):
#     stack = []
#     result = [0] * len(heights)
#
#     for idx in range(len(heights)-1, -1, -1): # 역순(우 -> 좌), 문제상에서 오른쪽에서 왼쪽으로 송신하므로.
#         current = (idx, heights[idx])         # 결과값 처리를 위해 index도 같이 저장
#
#         if (stack and len(stack) > 0):
#             for _ in range(len(stack)):       # 스택 내 모든 타워 확인
#                 peek = stack[-1]
#                 if current[1] >= peek[1] :    # 현재타워(수신타워) 높이 >= 스택타워(송신타워)이면 레이저 수신 가능
#                     result[peek[0]] = current[0] + 1     # 결과에 수신타워 위치 저장
#                     stack.pop()                          # 수신이 완료되면 스택에서 제거
#                
#         stack.append(current)                 # 추적할 대상 추가
#     return result


# 결론: while문으로 중복검사 최소화로 '성공'
def ReceivedTowers(heights):
    stack = []
    result = [0] * len(heights)

    for idx in range(len(heights)-1, -1, -1): 
        current = (idx, heights[idx])
        while len(stack) > 0 and current[1] >= stack[-1][1]:
            result[stack[-1][0]] = current[0] + 1
            stack.pop()               
        stack.append(current)
              
    return result

def main():
    N = int(input())
    Towers = list(map(int, input().split()))
    if N != len(Towers): return

    # ex) 6 9 5 7 4 => 0 0 2 2 4
    result = ReceivedTowers(Towers)
    print(" ".join(list(map(str, result))))

if __name__ == "__main__":
    main()
    