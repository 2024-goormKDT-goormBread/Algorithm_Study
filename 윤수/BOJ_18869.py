'''
문제제목: 멀티버스 II(http://acmicpc.net/problem/18869)
문제요약:
    각 우주의 수열은 같은 숫자의 빈도와 같은 순서를 유지해야 동일 구조로 인정된다.
    예를 들어 수열[2, 3, 1], [4, 5, 6]은 각 숫자의 상대적인 크기가 동일하므로 동일 구조로 간주된다.
    두 수열이 동일 구조인지 판별하는 문제
풀이방법:
    1. 수열의 길이와 수열을 입력받음
    2. 수열을 정렬하여 순서를 맞춤
    3. 수열을 문자열로 변환하여 딕셔너리에 저장
    4. 딕셔너리의 키를 정렬하여 순서를 맞춤
    5. 딕셔너리의 키를 순회하며 동일한 구조인지 확인
'''
import sys
input = sys.stdin.read

def normalize_sequence(seq):
    # 수열의 숫자에 대한 상대 순위 매기기
    sorted_indices = sorted(range(len(seq)), key=lambda x: seq[x])
    rank = [0] * len(seq)
    current_rank = 0
    for i in range(len(seq)):
        if i > 0 and seq[sorted_indices[i-1]] < seq[sorted_indices[i]]:
            current_rank += 1
        rank[sorted_indices[i]] = current_rank
    return tuple(rank)  # 변경 불가능한 튜플 형태로 반환

def main():
    data = input().split()
    M = int(data[0])  # 우주의 수
    N = int(data[1])  # 각 우주의 수열 길이
    index = 2
    sequences = []
    
    # 각 우주의 수열 입력받기
    for _ in range(M):
        seq = list(map(int, data[index:index + N]))
        index += N
        normalized = normalize_sequence(seq)
        sequences.append(normalized)
    
    # 각 수열의 구조 비교
    count = 0
    seen = {}
    for seq in sequences:
        if seq in seen:
            count += seen[seq]
            seen[seq] += 1
        else:
            seen[seq] = 1
            
    print(count)

if __name__ == "__main__":
    main()
