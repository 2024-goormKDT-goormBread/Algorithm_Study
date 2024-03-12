'''
문제제목: 가장 큰 증가 부분 수열(www.acmicpc.net/problem/11055)
문제요약:
    수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중 합이 가장 큰 것을 구하는 문제
    단, 수열 A는 1부터 시작한다.
'''
N = int(input())
A = list(map(int, input().split()))

dp = [x for x in A]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
    