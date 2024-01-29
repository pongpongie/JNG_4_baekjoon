import sys
input = sys.stdin.readline

cointypes = [0]
t = int(input())

for _ in range(t):
    n = int(input())
    cointypes = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j - cointypes[i-1] >= 0:
                dp[i][j] += dp[i][j-cointypes[i-1]]
    print(dp[n][m])
