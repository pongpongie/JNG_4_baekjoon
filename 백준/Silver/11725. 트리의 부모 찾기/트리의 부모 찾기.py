import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer[i]=v
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(answer[i])