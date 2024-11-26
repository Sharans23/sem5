import sys

V = 9  # Number of vertices in the graph

def initialize_single_source(dist, parent, visited, source):
    """Initializes the distances, parent, and visited arrays."""
    for i in range(V):
        dist[i] = sys.maxsize  # Set all distances to infinity
        parent[i] = -1         # Set all parent nodes to -1
        visited[i] = False     # Mark all nodes as unvisited
    dist[source] = 0           # Distance to source is 0


def min_distance(dist, visited):
    """Finds the vertex with the minimum distance value."""
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if not visited[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index


def relax(u, graph, dist, parent):
    """Relaxes the edges of the given vertex."""
    for v in range(V):
        if graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:  # Check if there is a shorter path
            dist[v] = dist[u] + graph[u][v]
            parent[v] = u


def dijkstra(graph, dist, visited, parent, source):
    """Performs Dijkstra's algorithm to find the shortest path."""
    for _ in range(V - 1):
        u = min_distance(dist, visited)  # Get the next vertex to process
        if u == -1:  # Break if no vertex is reachable
            break
        visited[u] = True               # Mark the vertex as processed
        relax(u, graph, dist, parent)   # Relax the edges of the vertex


def main():
    graph = [
        [0, 11, 0, 0, 0, 0, 0, 8, 0],
        [11, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 10, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 2, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 7],
        [0, 0, 0, 10, 0, 2, 0, 1, 6],
        [8, 0, 0, 0, 2, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 7, 6, 7, 0],
    ]

    source = 0  # Starting vertex
    dist = [0] * V
    parent = [0] * V
    visited = [False] * V

    initialize_single_source(dist, parent, visited, source)
    dijkstra(graph, dist, visited, parent, source)

    # Print the results
    print("Vertex\tDistance\tParent")
    for i in range(V):
        print(f"{i}\t\t{dist[i]}\t\t{parent[i]}")


if __name__ == "__main__":
    main()
