import sys
input = sys.stdin.readline

n = int(input())
number = input()
odd = 0
even = 0
for i in range(n):
    if number[i] == '2' or number[i] == '4' or number[i] == '6' or number[i] == '8' or number[i] == '0':
        even += 1
    else:
        odd += 1
if even>odd:
    print(0)
elif even < odd:
    print(1)
else:
    print(-1)