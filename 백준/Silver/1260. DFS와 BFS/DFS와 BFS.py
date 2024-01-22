import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    graph[a].sort()
    graph[b].sort()

visited_bfs = [False] * (n+1)
visited_dfs = [False] * (n+1)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

dfs(v)
print()
bfs(v)