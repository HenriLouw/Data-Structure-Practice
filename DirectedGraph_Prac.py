graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# we assume that this graph is acyclic
# hence we dont need to do any sort of visited data, we dont need to worry about any
# infinite cycles.


def DFT(graph, start, find):
    stack = [start]

    while stack:
        current_vertex = stack.pop()

        for v in graph[current_vertex]:
            if v == find:
                print("FOUND")
                break
            stack.append(v)

    print("NOT FOUND")

# a b d f c e


def BFT(graph, start):
    queue = [start]

    while queue:
        c_vertex = queue.pop()
        print(c_vertex)

        for v in graph[c_vertex]:
            queue.insert(0, v)


BFT(graph, 'a')