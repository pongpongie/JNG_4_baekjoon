import sys
input = sys.stdin.readline

def changes(a):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    quarters = a // 25
    a = a % 25
    dimes = a // 10
    a = a % 10
    nickels = a // 5
    a = a % 5
    pennies = a // 1
    a = a % 1

    print(quarters, dimes, nickels, pennies)


if __name__ == "__main__" :
    t = int(input())
    for _ in range(t):
        c = int(input())
        changes(c)