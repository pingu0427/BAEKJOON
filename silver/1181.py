import sys
input = sys.stdin.readline

lst = []
n = int(input())
for i in range(n):
    lst.append(input().rstrip())
lst = list(set(lst))
lst.sort()
lst.sort(key = len)
for i in range(len(lst)):
    print(lst[i])