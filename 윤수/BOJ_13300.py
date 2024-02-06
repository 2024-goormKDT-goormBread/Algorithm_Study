"""
// 문제분석 //
1학년~6학년 학생들 방 배정, 여학생은 여학생끼리, 남학생은 남학생끼리
한방에는 같은 학년의 학생만 배정, 한방에 한명도 가능
한방의 최대인원 K에 따른 방의 최소 개수 구하기

- 입력값
표준입력(공백구분)
ln 01. 수학여행에 참가하는 학생수 N(1<= N <= 1000) , 한 방에 배정할 수 있는 최대 인원 수 K(1<= N <= 1000)
ln 02~ 학생의 성별 S(0: 여학생, 1:남학생), 학년(1 <= Y <= 6) 

- 출력값
표준출력
학생 모두 배정하기 위한 최소한의 방의 수

"""

# 학생 수, 배정인원 수 입력
N, K = map(int, input().split())

# 학생목록 입력
studentList = []
for _ in range(N):
    studentList.append(tuple(map(int, input().split())))

# (성별, 학년)별로 학생 수 Dict 초기화
# ex. (여, 1학년) : 4명
counts = {} 
for gender in [0, 1]:
    for grade in range(1, 7): 
        counts[(gender, grade)] = 0 

# 학생 수 Dict 개수 세기
for gender, grade in studentList:
    counts[(gender, grade)] += 1

# 필요한 방 개수 구하기
totalRooms = 0
for count in counts.values():
    rooms = count // K
    if count % K != 0: # 나머지인원이 있으면 1씩 카운트
        rooms += 1     
    totalRooms += rooms

# 출력 
print(totalRooms)

