import sys
input = sys.stdin.readline

n = int(input())

subs_a = list(map(int, input().split()))
subs_b = list(set(subs_a))
subs_b.sort()
m = len(subs_b)

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if subs_a[j-1] == subs_b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[i][j])


