import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    word = input().strip('\n')
    array.append(word)

array = list(set(array))
array.sort()
array.sort(key = len)

for elem in array:
    print(elem)
