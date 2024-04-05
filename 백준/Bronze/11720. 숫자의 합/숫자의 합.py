# https://www.acmicpc.net/problem/11720
# 24.04.05 Thu
# day 100

import sys
input = sys.stdin.readline

n = int(input())

b = list(map(int, list(input().rstrip())))

print(sum(b))
