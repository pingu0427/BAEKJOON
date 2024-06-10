import sys
input = sys.stdin.readline

N, H, W = map(int,input().split())
lst = list(map(int,input().split()))

answer_width = 0
i = 0
while i+1 <= N-1 :
    answer_width += 2*W + min(lst[i],(W-lst[i+1])) - max(W+lst[i],(2*W-lst[i+1]))
    i += 2
print(answer_width*H)