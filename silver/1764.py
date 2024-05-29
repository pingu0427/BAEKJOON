import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
n_lst = set()
answer = []
for i in range(n):
    n_lst.add(sys.stdin.readline().rstrip())
for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a in n_lst:
        answer.append(a)
length = len(answer)
answer.sort()
print(length)
for i in range(length):
    print(answer[i])
    
    