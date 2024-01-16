n = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return n * factorial(n-1)

print(factorial(n))