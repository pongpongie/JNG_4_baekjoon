import sys
input = sys.stdin.readline

str_a = [0]
str_b = [0]
str_a.extend(list(input().strip()))
str_b.extend(list(input().strip()))

if len(str_b) > len(str_a):
    temp = str_b
    str_b = str_a
    str_a = temp

dp = [[0] * (len(str_a)) for _ in range(len(str_b))]

for i in range(1, len(str_b)):
    for j in range(1, len(str_a)):
        if str_a[j] == str_b[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str_b)-1][len(str_a)-1])