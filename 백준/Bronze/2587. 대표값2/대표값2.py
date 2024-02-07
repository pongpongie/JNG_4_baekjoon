import sys
input = sys.stdin.readline

def mean_median():
    a = []
    for _ in range(5):
        a.append(int(input()))
    a.sort()
    mean = sum(a) // 5
    median = a[2]
    print(mean)
    print(median)

if __name__ == "__main__":
    mean_median()