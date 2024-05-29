import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def lcm(a, b):
    while b > 0:
        r = a%b
        a, b = b, r
    return a

def gcd(a, b):
    return a*b//lcm(a,b)

print(lcm(a,b))
print(gcd(a,b))