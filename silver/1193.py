import sys
input = sys.stdin.readline

n = int(input())
line = 0
end = 0
while n > end:
    line += 1
    end += line
diff = end - n
if line%2 == 0:
    x = line - diff
    y = diff + 1
else:
    x = diff + 1
    y = line - diff
print("%d/%d"%(x,y))