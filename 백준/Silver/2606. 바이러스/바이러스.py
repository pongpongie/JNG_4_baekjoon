import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[]* (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [False] * (v+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
    return sum(visited)

print(dfs(1)-1)