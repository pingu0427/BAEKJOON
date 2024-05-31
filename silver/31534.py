import sys
import math

pi = math.pi
a,b,h = map(int, sys.stdin.readline().rstrip().split())
if a > b:
    a, b = b, a
elif a == b:
    print(-1)
    sys.exit()
answer = (h**2+(b-a)**2)*(b**2-a**2)/((a-b)**2)*pi
print(answer)