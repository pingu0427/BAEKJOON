import math
import sys

n = int(sys.stdin.readline().rstrip())
number = math.factorial(n)
answer = 0
number = str(number)
for i in range(len(number)):
    if number[-(i+1)] == '0':
        continue
    else:
        answer = number[-(i+1)]
        break
print(answer)