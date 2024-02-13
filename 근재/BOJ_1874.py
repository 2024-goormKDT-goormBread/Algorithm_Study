# 1~n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열을
# 만들 수 있다. 스택에 push 하는 순서는 반드시 오름차순을 지킨다고 가정
# 임의의 수열이 주어졌을 때, 스택을 이용해 그 수열을 만들 수 있는지
# 없는지, 있다면 어떤 순서로 push와 pop연산을 수행해야 하는지 알아낼 수 있다.
# 이를 계산하는 프로그램 작성
n = int(input())
temp = True
arr = []
stack = []
count = 1

for i in range(n):
    N = int(input())
    # N과 같은 수까지 count를 증가시켜서 push
    while count <= N:
        stack.append(count)
        arr.append('+')
        count += 1
    # stack의 Last 값이 N과 같으면 pop
    if stack[-1] == N:
        stack.pop()
        arr.append('-')
    # stack으로 만들 수 없는 수열이라면
    else:
        temp = False
        break

# temp의 상태에 따라 출력
if temp == False:
    print("NO")
else:
    for i in arr:
        print(i)

# 구현 포인트 1. 오름차순으로 push 연산을 한다. => for 문을 통해 오름차순으로 리스트에
# 값을 푸시한다.
# 구현 포인트 2. 첫 arr 배열과 같은 값이 나올 때 그 같은 값을 빼낸다.
# 여기서 고민 포인트 거꾸로 올라갈 수 있는 로직이 필요한가?
# 구현 포인트 3. 빼내다보면 인덱스가 거꾸로 감소하니까 다시 증가할 때 연산이 필요한데 이 불필요한
# 작업을 안 할 수 있는 방법이 있을까?
# 구현 포인트 4. 값을 끝까지 빼내는 로직.

# ++++--++-++-----
# [4, 3, 6, 8, 7, 5, 2, 1] / [1,2,5,3,4] 1 2 3 4 5 6 7 8
# 125 78
# 4 3 6 8 7 5 2 1