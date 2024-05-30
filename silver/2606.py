import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
answer = 0
lst = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    lst.append((a,b))
    
print(answer)
