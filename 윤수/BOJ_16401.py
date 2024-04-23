'''
문제제목: 과자 나눠주기(http://acmicpc.net/problem/16401)
문제요약:
    과자의 길이와 아이들의 수가 주어졌을 때, 모든 아이들이 같은 길이의 과자를 가질 수 있는 최대 길이를 구하는 문제
풀이방법: 
    1. 과자의 길이와 아이들의 수를 입력받음
    2. 아이들이 가질 수 있는 과자의 길이를 리스트에 저장
    3. 이분탐색을 통해 아이들이 가질 수 있는 최대 과자의 길이를 구함
    4. 결과 출력
'''
import sys
input = sys.stdin.read

def can_distribute(snacks, min_length, m):
    count = 0
    for snack in snacks:
        count += snack // min_length
        if count >= m:
            return True
    return False

def main():
    data = input().split()
    m = int(data[0])  # 조카의 수
    n = int(data[1])  # 과자의 수
    snacks = list(map(int, data[2:]))  # 과자들의 길이

    left, right = 1, max(snacks)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(snacks, mid, m):
            result = mid  # 가능한 경우 결과 저장
            left = mid + 1  # 최대 길이를 찾기 위해 범위를 늘림
        else:
            right = mid - 1  # 불가능한 경우 범위 줄임

    print(result)

if __name__ == "__main__":
    main()
