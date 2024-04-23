# 강을 건너는 하나의 차선을 n 개의 트럭이 건너려고 할 때
# 트럭의 순서 변경 불가, 트럭의 무게가 다름, 동시 w대의 트럭까지
# 다리의 길이는 w 단위길이 이며, 단위 시간에 하나의 단위 길이만큼 이동할 수 있다고 가정
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.
# 다리 위에 완전히 올라가지 못한 트럭의 무게는
# 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정

# 다리의 길이가 2, 최대 하중이 10이고 건너야 할 트럭의 무게가 [7,4,5,6]이면
# 7 건너고 45 같이 건너고 6 건너서 8이 된다.

# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때,
# 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성


n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

# 다리의 길이
bridge = [0] * w
# 시간
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    print(bridge)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(time)