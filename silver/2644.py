import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
num = 0
board = [[0]*n for _ in range(n+1)]
visit1 = ([0] * (100+1))
result = []
for i in range(m):
    x, y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(T,num):
    visit1[T] = 1
    num += 1
    if T == b:
        result.append(num)
    for i in board[T]:
        if visit1[i] == 0:
            dfs(i, num)
dfs(a,0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
