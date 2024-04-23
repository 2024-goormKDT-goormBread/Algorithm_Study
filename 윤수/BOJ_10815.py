'''
문제제목: 숫자카드(http://acmicpc.net/problem/10815)
문제요약:
    상근이가 가지고 있는 숫자카드에 다른 사람이 가지고 있는 숫자카드가 포함되어 있는지 확인하는 문제
풀이방법:
    1. 상근이가 가지고 있는 숫자카드를 입력받아 set에 저장
    2. 다른 사람이 가지고 있는 숫자카드를 입력받아 각 숫자가 상근이가 가지고 있는 숫자카드에 포함되어 있는지 확인
    3. 포함되어 있다면 1을, 아니라면 0을 출력
'''
n = int(input())
sanggeun_cards = set(map(int, input().split()))

m = int(input())
other_cards = list(map(int, input().split()))

result = []
for card in other_cards:
    if card in sanggeun_cards:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))