# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input())
sangeun = list(map(int, input().split()))

m = int(input())
guess = list(map(int, input().split()))

sangeun_dict = {}
for i in range(n):
    sangeun_dict[sangeun[i]] = 0

for elem in guess:
    if sangeun_dict.get(elem) == 0:
        print(1, end=' ')
    else:
        print(0, end=' ')
