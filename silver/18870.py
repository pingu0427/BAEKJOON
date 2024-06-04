import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
temp = list(sorted(set(lst)))
dic = {}
for i in range(len(temp)):
    dic[temp[i]] = i
for i in lst:
    print(dic[i], end=' ')