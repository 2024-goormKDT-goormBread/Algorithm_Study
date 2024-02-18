'''
AC는 정수배열에 연산을 하기위한 언어
이 언어에는 2가지 함수가 있다. R(뒤집기), D(버리기)
R함수는 배열에 있는 수의 순서를 뒤집는 함수, D함수는 첫번째 수를 버리는 함수(배열이 비어있으면 에러발생)
배열의 초기값과 수행할 함수가 주어졌을 때 최종결과를 구하는 프로그램을 작성하시오

-- 입력
첫재쭐에 테스트케이스의 T의 개수가 주어진다. T는 최대 100
각 테스트케이스 수행할 함수 p가 주어진다. p의 길이는 1보다 같고, 100000보다 작거나 같다
다음 줄에는 배열이 들어있는 수의 개수 n ( 0<=n<=100000)
다음줄에는 [x, ...] 과 같은 형태로 배열에 들어있는 정수가 주어진다. (1<= ㅌ <= 100)
전체 테스트케이스에 주어지는 p의 길이합과 n의 합은 70만을 넘기지않는다.

-- 출력
각 테스트케이스에 대해 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력, 에러가 발생한 경우 error 출력
'''

import sys
from collections import deque

def process(testCase):
    command = testCase[0]     # RDD
    length = int(testCase[1]) # 4
    
    # '['와 ']'을 지우고 deque로 치환
    items = deque(map(int, testCase[2].strip('[]').split(',')) if  testCase[2].strip('[]') else []) # [1,2,3,4]
    
    #### 채점결과(시간초과): Reverse 함수를 사용하는 경우 O(n)작업이 소요
    # for cmd in command:
    #     if cmd == "R": items.reverse()
    #     elif cmd == "D": 
    #         if not items: return "error"
    #         items.popleft()
    
    ### rever방향을 체크후, 그 방향에 따라 popleft, popright 결정 ####
    isReversed = False
    for cmd in command:
        if cmd == "R": isReversed = not isReversed # reversed 여부( True, False 전환)
        elif cmd == "D": 
            if not items: return "error"
            if isReversed: items.pop()  # reverse 이므로 뒤에서 pop
            else: items.popleft()       # 앞에서 pop
    
    if isReversed: items.reverse() # 최종 reverse 여부에 따라 item 나열
    return '[' + ','.join(map(str, items)) + ']'

def main():
    N = int(sys.stdin.readline().strip())
    lines = sys.stdin.read().splitlines() # 한번에 파일을 읽고 \n를 기준으로 split를 함
    
    # 라인별로 입력받은 리스트를 테스트케이스 단위로 튜플로 묶음
    # ex) ( RDD, 4, [1,2,3,4], ...)
    testCases = [(lines[i], lines[i+1], lines[i+2]) for i in range(0, len(lines), 3)]
    if len(testCases) != N: return
    
    result = [process(testCase) for testCase in testCases]
    print("\n".join(result))    

if __name__ == "__main__":
    main()

    