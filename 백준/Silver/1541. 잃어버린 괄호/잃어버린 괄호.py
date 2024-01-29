import sys
input = sys.stdin.readline

a = input().rstrip().split('-')

for i in range(len(a)):
    if '+' in a[i]:
        a[i] = sum(map(int, a[i].split('+')))
    else:
        a[i] = int(a[i])

if len(a) == 1:
    print(a[0])

else:
    for i in range(1, len(a)):
        a[0] -= a[i]
    print(a[0])
