import sys
input = sys.stdin.readline

a,b = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

c = factorial(a)//(factorial(b)*factorial(a-b))
print(c)