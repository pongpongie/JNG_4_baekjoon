import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

arr.sort(key = lambda x: int(x[0]))

for names in arr:
    print(names[0], names[1])