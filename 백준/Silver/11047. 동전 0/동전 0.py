import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cointypes = []

for _ in range(n):
    cointypes.append(int(input()))

a = reversed(cointypes)
cnt = 0

for coin in a:    
    cnt += k // coin
    k = k % coin
    if k == 0:
        print(cnt)
        break