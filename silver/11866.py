import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_lst = list(range(1,n+1))
i = 0
answer = []
while num_lst:
    i += k -1
    if i >= len(num_lst):
        i %= len(num_lst)
    answer.append(str(num_lst.pop(i)))
print('<',', '.join(answer),'>' ,sep = '')