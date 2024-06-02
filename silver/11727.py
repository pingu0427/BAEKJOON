input = sys.stdin.readline
n = int(input())
lst = [0]*(1001)
lst[1] = 1
lst[2] = 3
lst[3] = 5
lst[4] = 11
for i in range(5,n+1):
    lst[i] = 2*lst[i-2]%10007+lst[i-1]%10007
    lst[i] %= 10007
print(lst[n])