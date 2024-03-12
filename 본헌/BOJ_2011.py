import sys
input = sys.stdin.readline
data = list(map(int, input().rstrip()))
l = len(data)


if data[0] == 0:
  ans = 0

else:
  dp = [0] * (l + 1) # data 크기의 dp 배열 생성 후 [0:1]까지 1 할당
  dp[0], dp[1] = 1, 1
  
  for i in range(1, l):
    j = i + 1 # dp 인덱스
    if 0 < data[i]: # 1자리 계산
      dp[j] += dp[j-1]
    
    if 10 <= data[i] + data[i-1]*10 <= 26: # 2자리 계산
      dp[j] += dp[j-2]
    print(dp)
  ans = (dp[l] % 1000000)

print(ans)