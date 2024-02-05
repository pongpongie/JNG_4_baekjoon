# https://www.acmicpc.net/problem/2798

import sys
input = sys.stdin.readline

def blackjack():
    sum = 0
    result = []
    for i in range(n):
        sum += cards[i]
        for j in range(i+1, n):
            sum += cards[j]
            for k in range(j+1, n):
                sum += cards[k]
                result.append(sum)
                sum -= cards[k]
            sum -= cards[j]
        sum -= cards[i]
    return result



if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    result = blackjack()
    result.sort()
    for i in range(len(result)):
        if result[i] - m == 0 :
            print(result[i])
            break
        elif result[i] - m > 0 :
            print(result[i-1])
            break
    if result[-1] < m:
        print(result[i])