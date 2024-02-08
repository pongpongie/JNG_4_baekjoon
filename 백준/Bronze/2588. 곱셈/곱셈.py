import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

for i in range(2, -1, -1):
    print(int(a)*int(b[i]))

print(int(a)*int(b))