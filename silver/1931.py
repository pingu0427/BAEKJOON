import sys
input = sys.stdin.readline

N = int(input())
lst = []
cnt = 0

for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    lst.append((start, end))

lst.sort(key=lambda x : (x[1],x[0]))
cnt = 1
end = lst[0][1]
for i in range(1, N):
    if lst[i][0]>=end:
        end = lst[i][1]
        cnt += 1
    
print(cnt)