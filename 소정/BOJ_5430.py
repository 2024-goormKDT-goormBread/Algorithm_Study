import sys
from collections import deque


def que_setting(queue, arr):
  for i in map(int, arr[1:-1].split(',')):
    queue.append(i)

  return queue


def cal(func, queue):
  flag = 1
  for i in range(len(func)):
    if func[i] == 'R':
      flag = 0 if flag == 1 else 1
    elif func[i] == 'D':
      if len(queue) == 0:
        return print('error')
      else:
        queue.popleft() if flag == 1 else queue.pop()

  if flag == 0:
    queue.reverse()

  print('[', end='')
  print(*queue, sep=',', end='')
  print(']')


input = sys.stdin.readline
test_n = int(input())

for _ in range(test_n):
  func = list(str(input()))
  arr_n = int(input())
  arr = input().rstrip()

  queue = deque()
  if arr_n != 0:
    que_setting(queue, arr)
  cal(func, queue)