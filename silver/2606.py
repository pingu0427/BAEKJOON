import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
dfs_answer = 0
board1 = [[0]*n for _ in range(n)]
visit1 = ([0] * (1000+1))
for _ in range(m):
    x, y = map(int,input().split())
    board1[x-1][y-1] = 1
    board1[y-1][x-1] = 1

def dfs(T):
    visit1[T] = 1
    global dfs_answer
    for i in range(1,n+1):
        if board1[T-1][i-1] == 1 or board1[i-1][T-1] == 1:
            if visit1[i] == 0:
                visit1[i] = 1
                dfs_answer += 1
                dfs(i)
            

dfs(1)
print(dfs_answer)
