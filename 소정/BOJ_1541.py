# < 문제 >
# 첫째 줄에 식이 주어진다.
# 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있다.
# 가장 처음과 마지막 문자는 숫자이다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# < 풀이 > 
# '-' 이후에 '+'가 올 때,
# '-' 뒤에 괄호를 치면 괄호 안의 값들의 합이 
# 음수로 적용되기 때문에 최종 값이 작아지게 된다.

n = map(str, input().split('-')) # '-'를 기준으로 나누기
value = []

for i in n:
	sum = 0
	num = i.split('+') # '+' 기준으로 나누기
	for j in num:
		sum += int(j) # '+' 기준으로 나누어진 값을 더하기
	value.append(sum) # 더한 값을 value에 저장

result = value[0] # 처음에 오는 문자는 숫자이므로 더하고 시작
for i in range(1, len(value)):
	result -= value[i] #  '-' 기준으로 저장된 value 값이므로 각각이 값을 빼주기

print(result)
