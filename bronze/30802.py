import sys
input = sys.stdin.readline

n = int(input().rstrip())
s,m,l,xl,xxl,xxxl = map(int,input().split())
t,p = map(int,input().split())

a = 0
for i in [s,m,l,xl,xxl,xxxl]:
    if i != 0:
        if i%t == 0:
            a += i//t
        else:
            a += i//t + 1
b = n//p
c = n%p

print(a)
print(b, c)