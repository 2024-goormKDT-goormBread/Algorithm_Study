"""
1. 먼저 재귀를 몇번 돌건지 카운트 값 입력 
2. 0붜 whatisrecursion함수 돌리기 
3. 함수 내부 
- 재귀 숫자가 늘어날때마다 앞에 붙는 ____(언더바)가 늘어나는데, 처음엔 0을 곱해주기 때문에 언더바가 없음 
- 언더바 없이 내용 출력 후, n+1을 하여 재귀함수를 호출하여 다시 함수를 돌림 이떄는 n이 1이상이기 때문에 구문이 들어날 때마다 
언더바가 2배씩 증가하기 시작 
- 이렇게 재귀를 돌다가 만약 n값이 count값이랑 같아지게 된다면 마지막 질문에는 답변을 짧게 하기 때문에 긴 답변 대신 짧은 답변을 출력해주고 
이제부터 "라고 답변하였지" 단어를 출력해내며 해당 함수를 종료시킴
- 그 다음부터 이전 함수들도 차례로 종료되며 "라고 답변하였지"와 언더바를 줄여가며 출력하고 종료됨.
"""

def whatisrecursion(n):
    print("____"*n + '"재귀함수가 뭔가요?"')
    if n == count:
        print("____"*n+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        print("____"*n + "라고 답변하였지.")
        return
    print("____"*n + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("____"*n + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print("____"*n + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    whatisrecursion(n+1)
    print("____"*n + "라고 답변하였지.")

count = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
whatisrecursion(0)
