# +,-,괄호를 가지고 식을 만들었음. 그리고 괄호를 모두 지움
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 함

# 1. 식은 '0'~'9'그리고 -,+ 만으로 이루어져 있음
# 2. 가장 처음과 마지막 문자는 숫자이며 0으로 시작 가능 연속해서 두 개 이상의 연산자가 나타나지 않음
# 3. 5자리보다 많이 연속되는 숫자는 없음.
# 4. 입력은 <= 50

# -를 기준으로 값을 입력 받음
S = input().split('-')
arr = []
print(S)

for i in S:
    result = 0
    # +을 기준으로 또 나눔
    tmp = i.split("+")
    # 값들을 더한 후에 arr에 값을 저장함
    for j in tmp:
        result += int(j)
    arr.append(result)

# 맨 처음 요소는 숫자이므로 n으로 빼줌
n = arr[0]

# n에서 값을 계속 뺌
for i in range(1,len(arr)):
    n -= arr[i]
print(n)


