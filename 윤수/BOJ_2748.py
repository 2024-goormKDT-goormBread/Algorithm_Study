'''
피보나치 수2: https://www.acmicpc.net/problem/2748
문제 요약:
    n이 주어졌을 때, n번째 피보나치 수를 구하는 문제
    단, n은 90보다 작거나 같은 자연수

'''
n = int(input())

fib = [0, 1] 

for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])

print(fib[n])