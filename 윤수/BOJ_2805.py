'''
문제제목: 나무 자르기(http://acmicpc.net/problem/2805)
문제요약:
    상근이는 나무 M미터를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 문제
풀이방법:  
    1. 나무의 높이를 입력받음
    2. 이분탐색을 통해 절단기에 설정할 수 있는 높이의 최댓값을 구함
    3. 결과 출력
'''
import sys
input = sys.stdin.readline

def total_wood(trees, height):
    return sum(max(0, tree - height) for tree in trees)

def find_max_height(trees, m):
    low, high = 0, max(trees)
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if total_wood(trees, mid) >= m:
            best = mid  # 가능한 최대 높이 갱신
            low = mid + 1
        else:
            high = mid - 1

    return best

def main():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    result = find_max_height(trees, m)
    print(result)

if __name__ == "__main__":
    main()
