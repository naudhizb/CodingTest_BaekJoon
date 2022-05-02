

graph_list = {
    1: set([3, 4]),
    2: set([3, 4, 5]),
    3: set([1, 5]),
    4: set([1]),
    5: set([2, 6]),
    6: set([3, 5])
}

root_node = 1


### BFS

from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


print(BFS(graph_list, root_node))


### DFS with stack

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


print(DFS(graph_list, root_node))


## DFS with recursive function call

def DFS_recursive(graph, v, visited=[]):
    visited.append(v)
    for w in graph_list[v]:
        if not w in visited:
            visited = DFS_recursive(graph, w, visited)
    return visited


print(DFS_recursive(graph_list, root_node))
