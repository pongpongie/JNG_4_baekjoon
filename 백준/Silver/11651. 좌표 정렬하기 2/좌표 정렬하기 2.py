import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x]);

arr.sort()

for i in arr:
    print(i[1], i[0]);