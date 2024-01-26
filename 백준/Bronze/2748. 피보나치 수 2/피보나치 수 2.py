import sys
input = sys.stdin.readline

def fibo2(num : int) -> int:
    cnt = [0, 1, 1]
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        for i in range(3, num+1):
            cnt.append(cnt[i-1] + cnt[i-2])
    return cnt[num]

print(fibo2(int(input())))