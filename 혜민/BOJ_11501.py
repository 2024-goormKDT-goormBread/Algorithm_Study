T = int(input())

for t in range(T):

    N = int(input())
    price = list(map(int, input().split()))

    money = 0 

    maxPrice = 0 # 주식 최대 가격
    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice= price[i]
        else: # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
            money += maxPrice - price[i]

    print(money)
