import sys

input = sys.stdin.readline
n = int(input())
lst = [0]*(1001)
lst[1] = 1
lst[2] = 2
for i in range(3,n+1):
    lst[i] = lst[i-2]%10007+lst[i-1]%10007
    lst[i] %= 10007
print(lst[n])