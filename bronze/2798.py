import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
summ = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            new_summ = lst[i] + lst[j] + lst[k]
            if new_summ <= m and new_summ > summ:
                summ = new_summ
print(summ)