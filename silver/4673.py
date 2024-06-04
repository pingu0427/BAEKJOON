def d(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

s = list(range(1,10001))
for n in range(1,10001):
    if d(n) in s:
        s.remove(d(n))
    
for i in range(len(s)):
    print(s[i])