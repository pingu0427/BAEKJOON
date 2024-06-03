import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n, m, v = map(int, input().split())
board1 = [[0]*n for _ in range(n)]
board2 = [[0]*n for _ in range(n)]
visit1 = ([0] * (1000+1))
visit2 = ([0] * (1000+1))
for _ in range(m):
    x, y = map(int,input().split())
    board1[x-1][y-1] = 1
    board2[x-1][y-1] = 1
    board1[y-1][x-1] = 1
    board2[y-1][x-1] = 1
dfs_answer = [v]
bfs_answer = [v]

def dfs(T):
    visit1[T] = 1
    for i in range(1,n+1):
        if board1[T-1][i-1] == 1 or board1[i-1][T-1] == 1:
            if visit1[i] == 0:
                visit1[i] = 1
                dfs_answer.append(i)
                dfs(i)
            
def bfs(T):
    visit2[T] = 1
    queue.append(T)
    while queue:
        T = queue.popleft()
        for i in range(1,n+1):
            if board2[T-1][i-1] == 1 or board2[i-1][T-1] == 1:
                if visit2[i] == 0:
                    visit2[i] = 1
                    bfs_answer.append(i)
                    queue.append(i)
            

dfs(v)
bfs(v)
print(*dfs_answer)
print(*bfs_answer)