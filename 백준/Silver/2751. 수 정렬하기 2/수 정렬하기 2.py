import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

num.sort()
for nums in num:
    print(nums)