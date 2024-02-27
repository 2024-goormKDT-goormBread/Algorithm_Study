'''
4개 기호 (,),[,] 로 만들어진 올바른 괄호열은 다음과 같이 정의된다.
1. 한 쌍의 괄호로만 이루어진 (), [] 모두 올바른 괄호열
2. x가 올바른 괄호열이면, (x), [x]도 올바른 괄호열
3. x, y 모두 올바른 괄호열이면, 이들을 결합한 xy도 올바른 괄호열, 괄호값은 아래와 같다.
    - ()의 괄호값은 2
    - []의 괄호값은 3
    - (x)의 괄호값은 x값의 2배    (x가 올바르다는 전제하)
    - [x]의 괄호값은 xr값의 3배   (x가 올바르다는 전제하)
    - XY의 결합된 괄호값은 X+Y
    ex. (()[[]])([]) 의 괄호값은 (()[[]]) + ([]) = 2X(2+3X3) + 6 = 28

-- 입력: 첫째 줄에 괄호열을 나타내는 문자열(길이는 1 이상 30 이하)
-- 출력: 괄호값을 나타내는 정수, 입력이 올바르지 않으면 0을 출력
'''
import sys

def calculateBrackets(brackets: str) -> int:
    stack = []                   # 페어가 확인되지 않은 여는괄호(,[ 추적하기 위한 스택
    pair = {')': '(', ']': '['}  # 괄호의 짝(닫는 괄호를 키로)을 딕셔너리로 매핑
    score = {')': 2, ']': 3}     # 괄호의 종류에 따른 점수를 딕셔너리로 매핑
    temp = 1                     # 현재 깊이에서의 임시 점수
    result = 0 

    for i, char in enumerate(brackets):  # index와 value를 모두 가져오기위해 enumerate 함수 사용
        if char in "([":                 
            stack.append(char)           # 여는 괄호가 있다면 스택(추적대상)에 추가
            
            # 여는괄호(,[ 인 경우 추후 잠재적으로 괄호쌍-(), []이 포함될 수 있기 때문에 temp에 임시점수 저장
            # (x)의 괄호값은 x값의 2배, [x]의 괄호값은 x값의 3배
            # 즉 여는괄호가 많아질수록(중첩깊이가 깊어질수록) 점수는 배로 증가된다
            if char == '(': 
                temp = temp * 2    # 소괄호이므로 점수를 2배
            else:
                temp = temp * 3    # 대괄호이므로 점수를 3배

        elif char in ")]":
            # 스택이 비었거나(=스택에 여는 괄호가 없음), 괄호가 서로 맞지 않은 경우 0 반환
            if not stack or stack[-1] != pair[char]:
                return 0
            
            # 매칭된 괄호쌍(), []에 대해서는 확정된 점수를 result에 추가
            # 처음 닫는괄호가 나왔을 때 점수가 유지되고 이후 닫는 괄호가 나오면 무시된다.
            # 예를 들어 (([] 일때 괄호가 유효하다는 가정하, result 수는 12로 유지된다.
            if i > 0 and brackets[i - 1] == pair[char]:
                result = result + temp
            
            stack.pop()    # 괄호가 매치되었으므로 스택(추적대상)에서 제거 
            
            # 현재 깊이에서 닫는괄호로 인해 매칭완료되었으로 중첩된 점수는 반전된다.
            # 예를들어 (([] 일때 2x2x3에서 매칭된 괄호[] 이후는 2x2이다. 마지막까지 유효하면 temp는 1이 된다.
            temp = temp // score[char]  

    # 마지막까지 스택(여는 괄호)가 남아있는 경우 0 반환
    if stack: return 0
    
    return result
        
def main():
    inputData = sys.stdin.readline().strip()
    outputData = calculateBrackets(inputData)
    print(outputData)   

if __name__ == "__main__":
    main()