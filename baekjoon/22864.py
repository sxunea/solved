import sys
a,b,c,m = map(int, sys.stdin.readline().split())
p = 0
w = 0

if (a>m):
  w = 0
else:
  for i in range(1,25):
    if p+a <= m:
      p += a
      w += b
    else:
      if p-c >= 0:
        p -= c
      else:
        p = 0
print(w)
  