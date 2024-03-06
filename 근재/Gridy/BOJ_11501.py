# 1. 주식 하나를 산다.
# 2. 원하는 만큼 가지고 있는 주식을 판다.
# 3. 아무 것도 안한다.

# 날 별로 주식의 가격을 알려 주었을 때, 최대 이익이 얼마나 되는지 계산해 달라고 부탁함

# 예를 들어 날 수가 3일이고 날 별로 주기가 10,7,6일 때, 주기가 계속 감소하므로
# 최대 이익은 0이 된다.
# 그러니 만약 날 별로 주가가 3,5,9일 때 처음 두 날에 주식을 하나씩 사고, 마지막 날 다
# 팔면 이익이 10이 된다.
# 3에서 주식을 사고 5가 됐으니 2가 이득이니 2, 5에서 주식을 또 샀는데 5에서 9까지 주식이
# 올랐을 때 4의 이득을 두 주가 8의 이득을 봤으니 총 이익은 10이다.

# 값이 떨어졌을 때 팔면 된다.
# 아이디어
# 1. i보타 i+1이 클 때 - i+1 - i 를 하고 값을 넣는다. 여기서 값이 두 개이상일 때는 요소의 갯
# 수를 곱해주어야 한다.
# 2. 값이 똑갈을 때 - 그냥 값을 넣기만 한다.
# 3. 값이 떨어졌을 때 - 배열에 저장된 값을 모두 더하고 배열을 비운다.
import sys

T = int(input())
for i in range(T):
    N = int(sys.stdin.readline().rstrip("\n"))
    days = list(map(int, sys.stdin.readline().rstrip("\n").split()))
    stock = 0
    result = 0

    for i in range(len(days) - 1, -1, -1):
        if days[i] > result: # 9
            result = days[i]
        else:
            stock += result - days[i] # 9
    print(stock)

    # for i in range(0,len(days)-1):
    #     print("days[i]: ",days[i])
    #     if days[i] < days[i+1]:
    #         if len(stock) >= 1 :
    #             stock.append((days[i + 1] - days[i]) * (len(stock)+1))
    #             continue
    #         stock.append(days[i+1] - days[i])
    #     elif days[i] == days[i+1]:
    #         stock.append(days[i])
    #     else:
    #         result += sum(stock)
    #         stock = []
    #     print("stock: ",stock)
    # if len(stock) > 0:
    #     result += sum(stock)
    #     stock = []
    # print(result)

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 6
# 1 1 3 1 2 5
