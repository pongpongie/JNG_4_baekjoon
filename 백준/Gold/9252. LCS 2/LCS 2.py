import sys
from collections import deque

result = deque()
input = sys.stdin.readline

string_a = list(map(str, input().strip()))
string_b = list(map(str, input().strip()))

dp = [[0] * (len(string_a)+1) for _ in range(len(string_b)+1)]

for i in range(1, len(string_b)+1):
    for j in range(1, len(string_a)+1):
        if string_a[j-1] == string_b[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(string_b)][len(string_a)])
ans = []

while dp[i][j] != 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        dp[i][j] == dp[i-1][j-1]
        ans.append(string_b[i-1])
        i -= 1
        j -= 1

ans.reverse()

for answer in ans:
    print(answer, end='')