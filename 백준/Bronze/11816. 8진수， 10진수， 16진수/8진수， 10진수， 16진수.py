import sys
input = sys.stdin.readline

x = input().rstrip()

if len(x) >= 2:
    if (x[0] == "0") & (x[1] == "x"):
        print(int(x[2:], 16))
    elif x[0] == "0":
        print(int(x[1:], 8))
    else:
        print(int(x))
else:
    print(int(x))
        