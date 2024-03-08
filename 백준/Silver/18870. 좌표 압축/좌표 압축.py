# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data2 = sorted(list(set(data)))
dic = {data2[i] : i for i in range(len(sorted(data2)))}

for elem in data:
    print(dic[elem], end=' ')