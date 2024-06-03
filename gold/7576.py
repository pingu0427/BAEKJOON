import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

m, n = map(int, input().split())
board = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
all_ripe = True
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((j,i))
        else:
            all_ripe = False
            
if all_ripe:
    print(0)
    sys.exit()

def bfs():
    date = -1
    while queue:
        date += 1
        for i in range(len(queue)):
            x_num,y_num = queue.popleft()
            if -1<x_num<m and -1<y_num<n:
                for k in range(4):
                    nx, ny = x_num+dx[k], y_num+dy[k]
                    if 0 <= nx <m and 0 <= ny <n and board[ny][nx] == 0:
                        board[ny][nx] = 1
                        queue.append((nx,ny))
    for row in board:
        if 0 in row:
            return -1
    return date

print(bfs())

