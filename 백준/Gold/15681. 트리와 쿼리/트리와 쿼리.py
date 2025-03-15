import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, R, Q = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree_size = [0] * (N + 1)
visited = [False] * (N + 1)


def dfs(node, parent=-1):
    visited[node] = True
    subtree_size[node] = 1
    for child in graph[node]:
        if not visited[child] and child != parent:
            subtree_size[node] += dfs(child, node)
    return subtree_size[node]


dfs(R)
for _ in range(Q):
    i = int(input())
    print(subtree_size[i])
