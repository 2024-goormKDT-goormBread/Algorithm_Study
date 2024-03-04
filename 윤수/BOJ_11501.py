'''
홍준이는 주식에 푹 빠졌다. 그는 아래 세가지 중 한 행동을 한다.
1. 주식 하나를 산다
2. 원하는 만큼 가지고 있는 주식을 판다
3. 아무것도 안한다.
날 별로 주식의 가겨을 알려주었을 때, 최대 이익이 얼마나 되는지 계산해달라고 한다.

예를 들어 
날수가 3일, 날 별로 주가 10, 7,6 일때, 주가감소로 인해 최대 이익은 0이다.
만약 주가 3, 5, 9일때 처음 두날에 주식을 하나씩 사고, 마지막 날에 다 팔아 버리면 이익이 10이 된다.

-- 입력
테스트 케이스 T, 날의 수N, 날별 주가 N개의 자연수
-- 출력
각 테스트 케이스에 대해 최대 이익을 출력
'''
import sys

def maxProfit(prices):
    max_profit = 0        # 최대 이익 초기화
    max_future_price = 0  # 미래의 최대 주가 초기화

    for price in reversed(prices):    # 미래의 최대주가를 계산하기 위해 역순으로 순회
        if price > max_future_price:  # 현재 주가가 미래의 최대 주가보다 클때
            max_future_price = price  
        max_profit = max_profit + (max_future_price - price)  # 이익 계산 및 추가

    return max_profit

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        if N < 2 or N > 1000000: return
        
        prices = list(map(int, sys.stdin.readline().strip().split()))
        if len(prices) != N: return
        
        print(maxProfit(prices))
        
if __name__ == "__main__":
    main()