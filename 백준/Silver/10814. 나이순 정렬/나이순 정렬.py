# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())
    arr[i][0] = int(arr[i][0])
    arr[i].append(i)

arr.sort(key = lambda x: (x[0], x[2]))

for names in arr:
    print(names[0], names[1])