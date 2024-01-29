import sys
input = sys.stdin.readline

def fibo2(num : int) -> int:
    cnt = [0, 1]
    for i in range(2, num+1):
        cnt.append(cnt[i-1] + cnt[i-2])
    return cnt[num]

print(fibo2(int(input()))) 




