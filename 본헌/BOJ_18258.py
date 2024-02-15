# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys
from collections import deque
N = int(input())
queue, ans = deque([]), []
for _ in range(N):
    S = sys.stdin.readline().split()
    if S[0] == 'push':
        queue.append(S[1])

    elif S[0] == 'pop':
        if queue:
            ans.append(queue.popleft()) #큐 pop 함수시 시간초과
        else:
            ans.append('-1')

    elif S[0] == 'size':
        ans.append(len(queue))

    elif S[0] == 'empty':
        if queue:
            ans.append('0')
        else:
            ans.append('1')

    elif S[0] == 'front':
        if queue:
            ans.append(queue[0])
        else:
            ans.append('-1')

    elif S[0] == 'back':
        if queue:
            ans.append(queue[-1])
        else:
            ans.append('-1')

for val in ans:
    print(val)


