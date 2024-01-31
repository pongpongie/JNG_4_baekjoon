import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cnt = n
    rank = [[0, 0] for _ in range(n)]
    for i in range(n):
        document, interview = map(int, input().split())
        rank[i][0] = document
        rank[i][1] = interview
    rank.sort()
    cnt = 1
    max_ = rank[0][1]
    for i in range(1, n):
        if max_ > rank[i][1]:
            cnt += 1
            max_ = rank[i][1]
            
    print(cnt)