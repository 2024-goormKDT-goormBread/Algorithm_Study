'''
문제제목: 차집합(http://boj.kr/1822)
문제요약:
    두 집합 A, B가 주어졌을 때, A-B를 구하는 문제
풀이방법:  
    1. 집합 A, B를 입력받아 set에 저장
    2. A-B를 구한 후, 정렬하여 출력
'''
# 입력 받기
n, m = map(int, input().split())  # 두 집합 A와 B의 크기
A = set(map(int, input().split()))  # 집합 A
B = set(map(int, input().split()))  # 집합 B

# A에서 B를 뺀 차집합 계산
difference = sorted(A - B)

# 결과 출력
print(len(difference))  # 차집합의 요소 개수 출력
if difference:
    print(' '.join(map(str, difference)))  # 차집합의 요소 오름차순 출력
else:
    print()  # 차집합이 비어있으면 빈 줄 출력
