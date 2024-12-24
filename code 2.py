
def prims_algorithm(graph):
    # Step 1: Initialize
    num_vertices = len(graph)
    selected_vertices = [False] * num_vertices
    selected_vertices[0] = True
    mst_edges = []

    # Step 2: Select Edge
    for _ in range(num_vertices - 1):
        min_edge = (None, None, float('inf'))
        for u in range(num_vertices):
            if selected_vertices[u]:
                for v, weight in enumerate(graph[u]):
                    if not selected_vertices[v] and weight < min_edge[2]:
                        min_edge = (u, v, weight)

        # Step 3: Add Edge
        u, v, weight = min_edge
        mst_edges.append((u, v, weight))
        selected_vertices[v] = True

    return mst_edges

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst = prims_algorithm(graph)
print("Edges in MST:", mst)
