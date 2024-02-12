import sys
sys.stdin.readline

def cutline(n, k):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[n-k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    cutline(n, k)