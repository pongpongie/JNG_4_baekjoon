import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cointypes = []

for _ in range(n):
    cointypes.append(int(input()))

cointypes.sort(reverse=True)

rest = 0
cnt = 0

for i in range(n):
    if i == 0:
        cnt += k // cointypes[i]
        rest = k % cointypes[i]
    elif i != 0:
        cnt += rest // cointypes[i]
        rest = rest % cointypes[i]
    if rest == 0:
        print(cnt)
        break