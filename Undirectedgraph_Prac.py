graph = {
    'a': ['c', 'b'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['b', 'f'],
    'e': ['c'],
    'f': ['d']
}


def DFT(graph, start):
    stack = [start]
    visited = []

    while stack:
        current_v = stack.pop()
        visited.append(current_v)
        print(current_v)
        for v in graph[current_v]:
            if v not in visited:
                stack.append(v)


def BFT(graph, start) -> None:
    queue = [start]
    visited = []

    while queue:
        current_v = queue.pop()
        visited.append(current_v)

        for v in graph[current_v]:
            if v not in visited:
                queue.insert(0, v)