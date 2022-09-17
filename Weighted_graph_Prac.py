weighted_graph = {
    'RSA': [['LON', 1], ['JPN', 1]],
    'LON': [['JPN', 3]],
    'JPN': [["USA", 4]],
    'USA': [["RSA", 5]]
}


def DFT(graph, start):
    stack = [start]

    visited = []

    while stack:
        current, weight = stack.pop()

        visited.append(current)

        print(f'LOC:{current},WEIGHT:{weight}')

        for v, w in graph[current]:

            if v not in visited:
                stack.append([v, w])


DFT(weighted_graph, ['RSA', 0])