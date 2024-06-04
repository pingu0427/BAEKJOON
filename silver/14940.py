from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
queue = deque([])
visit = [[False]*M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        if row[j] == 2:
            queue.append((j, i, 0))
            visit[i][j] = True
            row[j] = 0
    board.append(row)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs():
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx,ny,d = v[0]+dx[i],v[1]+dy[i],v[2]+1
            if -1<nx<M and -1<ny<N:
                if visit[ny][nx] == False:
                    if board[ny][nx] == 1:
                        queue.append((nx,ny,d))
                        visit[ny][nx] = True
                        board[ny][nx] = d
    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and board[i][j] == 1:
                board[i][j] = -1

bfs()
for i in range(N):
    print(*board[i])       
        
    