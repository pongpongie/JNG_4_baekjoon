import sys
input = sys.stdin.readline

n = int(input())
bag = [0, 3, 5]
dp = [-1 for _ in range(n+1)]

for i in range(1, len(bag)):
    for j in range(1, n+1):
        if j % bag[i] == 0:
            dp[j] = j // bag[i]
        elif j % bag[i] != 0:
            if j - bag[i] > 0 and dp[j - bag[i]] != -1:
                dp[j] = dp[j - bag[i]] + 1

print(dp[-1])


                    