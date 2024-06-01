import sys

n = int(sys.stdin.readline().rstrip())
lst = [1,3]+[0]*(n-1)
if n == 1:
    print(3)
else:
    for i in range(2,n+1):
        lst[i] = (lst[i-2] + 2*lst[i-1])%9901
    print(lst[n])