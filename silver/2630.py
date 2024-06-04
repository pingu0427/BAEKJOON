import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
w_count = 0
b_count = 0
size = N

def dc(x,y,N):
    global w_count
    global b_count
    tmp = board[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if board[i][j] != tmp:
                dc(x,y,N//2)
                dc(x,y+N//2,N//2)
                dc(x+N//2,y,N//2)
                dc(x+N//2,y+N//2,N//2)
                return
    else:
        if tmp == 0:
            w_count += 1
        else:
            b_count += 1

dc(0,0,N)
print(w_count)
print(b_count)