import sys

input = sys.stdin.readline

n, c, w = map(int, input().rstrip().split())

lst = []
max_cut_count = 0
max_len_count = 0
max_price = 0

for i in range(n):
    a = int(input().rstrip())
    lst.append(a)

for k in range(1,max(lst)+1):
    price = [0]*n
    new_cut_count = 0
    new_len_count = 0
    for j in range(n):
        if lst[j]%k == 0:
            new_cut_count = (lst[j]-1)//k
        else:
            new_cut_count = lst[j]//k
        new_len_count = lst[j]-lst[j]%k
        if new_len_count*w - new_cut_count*c > price[j]:
            price[j] = new_len_count*w - new_cut_count*c
    if sum(price) > max_price:
        max_price = sum(price)

print(max_price)