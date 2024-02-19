import sys
input = sys.stdin.readline

num_list = [0] * 10001

n = int(input())

for i in range(n):
    val = int(input())
    num_list[val] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)