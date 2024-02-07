n,k=map(int,input().split())
student = [[0] * 6 for _ in range(2)] 
'''
def 데이터(num):
    if num == n:
        return

    s, y = map(int, input().split())
    student[s][y-1] += 1

    데이터(num+1)

데이터(0)
'''
for i in range(0,n):
    s, y = map(int, input().split())
    student[s][y-1] += 1

count = 0
for i in range(2):
    for j in range(6):
        if(student[i][j]%k == 0):
            count += student[i][j]/k
        else:
            count += student[i][j]//k + 1
    
print(int(count))
