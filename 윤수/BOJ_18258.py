'''
큐 구현하기
push: 정수 x를 넣는다
pop: 큐에서 가장 앞에서 있는 정수를 빼고, 그 수를 출력, 없는 경우 -1
emptty: 큐가 비어 있으면 1, 아니면 0
front: 큐가의 가장 앞쪽의 정수, 없으면 -1
back: 큐의 가장 뒤에 있는 정수를 출력, 없으면 -1
size: 큐에 들어가있는 정수 개수

-- 입력
첫번째 줄에 명령의 수 N
둘째줄부터 N개의 줄에 명령 하나씩 추가
주어진 정수는 1보다 같고, 100,000보다 작거나 같다.

-- 출력
출력해야하는 명령이 주어질때마다 한줄에 하나씩 출
'''
import sys
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.popleft() if self.items else -1

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if not self.items else 0

    def front(self):
        return self.items[0] if self.items else -1

    def back(self):
        return self.items[-1] if self.items else -1
    
def process(commands):
    queue = Queue()
    output = []
    
    for command in commands:
        cmd = command.split()
        if cmd[0] == "push":
            queue.push(cmd[1])
        elif cmd[0] == "pop":
            output.append(queue.pop())
        elif cmd[0] == "size":
            output.append(queue.size())
        elif cmd[0] == "empty":
            output.append(queue.empty())
        elif cmd[0] == "front":
            output.append(queue.front())
        elif cmd[0] == "back":
            output.append(queue.back())
    return output

N = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().strip() for _ in range(N)]
results = process(commands)
print('\n'.join(map(str, results)))