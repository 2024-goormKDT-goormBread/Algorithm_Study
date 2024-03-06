n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)

position = [0 for _ in range(n+1)]
for i in range(1,n+1):
	position[arr[i]] = i

count = 1
max_length = -1

for i in range(1, n):
	if position[i] < position[i+1]:
		count += 1
		if count > max_length:
			max_length = count
	else:
		count = 1

print(n-max_length)