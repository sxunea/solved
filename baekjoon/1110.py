n = int(input())
key = n
ans = 0

while True:
    ans += 1
    A = n//10 + n%10
    n = n%10*10 + A%10
    if (n == key):
        break
print(ans)