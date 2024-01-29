import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

a = reversed(coins)
cnt = 0

for coin in a:
    if K // coin:
        cnt += K//coin
        K %= coin

print(cnt)