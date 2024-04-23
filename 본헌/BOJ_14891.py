from collections import deque
import sys
input = sys.stdin.readline
board = [deque(map(int, input().rstrip())) for _ in range(4)]
k = int(input())
def left_rotate(idx, way):
  if idx < 0:
    return
  
  if board[idx][2] != board[idx + 1][6]:
    left_rotate(idx - 1, -way)
    board[idx].rotate(way)

def right_rotate(idx, way):
  if idx > 3:
    return
  
  if board[idx - 1][2] != board[idx][6]:
    right_rotate(idx + 1, -way)
    board[idx].rotate(way)

def select_rotate(idx, way):
  board[idx].rotate(way)
  
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    left_rotate(a - 1, -b)
    right_rotate(a + 1, -b)
    select_rotate(a, b)


res = 0
for i in range(4):
  if board[i][0] == 1:
    res += 2**i

print(res)