import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
sum = [0]
tmp = 0
for i in lst:
    tmp += i
    sum.append(tmp)

answer = 0
for j in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer = sum[b] - sum[a-1]
    print(answer)