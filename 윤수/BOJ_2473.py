'''
문제제목: 세 용액(http://acmicpc.net/problem/2473)
문제요약:
    N개의 용액이 주어졌을 때, 세 용액을 섞어 0에 가장 가까운 용액을 만드는 문제
풀이방법:  
    1. 용액의 수와 용액을 입력받음
    2. 용액을 정렬한 후, 세 용액을 선택하여 0에 가장 가까운 용액을 만드는 방법을 찾음
    3. 결과 출력
'''
import sys
input = sys.stdin.readline  

def find_zero_combo(solutions):
    solutions.sort()            # 용액을 오름차순으로 정렬
    n = len(solutions)
    closest_sum = float('inf')  # 0에 가까운 용액의 합(초기값: 무한대)
    result = []
    
    for i in range(n-2):
        left, right = i + 1, n - 1  # 투 포인터 초기화
        
        while left < right:
            current_sum = solutions[i] + solutions[left] + solutions[right]
            
            # 현재 합이 이전 합보다 0에 더 가까우면 결과 갱신
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = [solutions[i], solutions[left], solutions[right]]
                
            # 현재 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
            if current_sum < 0:
                left += 1
                
            # 현재 합이 0보다 크거나 같으면 오른쪽 포인터를 왼쪽으로 이동
            else:
                right -= 1
                
            # 현재 합이 0이면 반복 종료
            if closest_sum == 0:
                break
            
        # 현재 합이 0이면 반복 종료
        if closest_sum == 0:
            break
    
    return result

def main():
    n = int(input()) 
    solutions = list(map(int, input().split()))
    result = find_zero_combo(solutions)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
