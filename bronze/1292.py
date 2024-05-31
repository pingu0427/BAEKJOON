import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
n = 0
lst = [0]
while n <= b:
    n += 1
    for i in range(n):
        lst.append(n)
answer = 0
for i in range(a,b+1):
    answer += lst[i]
print(answer)
