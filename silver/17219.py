import sys
input = sys.stdin.readline

dic = {}
n,m = map(int, input().split())
for i in range(n):
    a, b = input().split()
    dic[a] = b
for i in range(m):
    find = input().rstrip()
    print(dic[find])