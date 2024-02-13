"""
// 문제분석
재민이(장부관리담당), 재현이(돈관리지원)
재현이 잘못된 수를 부를 때마다 0을 외쳐서, 재민이가 가장 최근에 쓴 수 지움
재민이는 모든 수를 받아 적은 후 그 수의 합을 알고싶다.

- 입력값
첫번재줄 정수가 주이짐(1 <= K <= 100,000)
이후, K개 줄에 정수N 1개씩 주어짐. ( 0 < N < 1,000,000 )
정수N이 0 일경우 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다
정수N이 0일 경우 지울수 있음을 보장

- 출력값
재민이가 최종적으로 적어낸 수의 합을 출력 
최종적으로 적어낸 수의 합은 2**31-1보다 작거나 같은 정수
"""

# dataList값이 0이면 최근값을 지움
def checkNumbers(dataList):
    stack = []
    for number in dataList:
        if number == 0:
            if len(stack) == 0: break # 스택이 비어있는 경우 종료
            stack.pop();
        else:
            stack.append(number)
    return stack

def main():
    K = int(input())
    if K < 1 or K > 100000: return
    
    jh_Data = [int(input()) for i in range(K)]  #재현의 데이터
    jm_Data = checkNumbers(jh_Data)             #재민의 데이터
    
    res = sum(jm_Data)
    if res <= 2**31-1: print(res)  # 결과값은 2**31-1보다 작거나 같은 정수

if __name__ == "__main__":
    main()
    