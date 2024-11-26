import sys

def bellman_ford(graph, V, E, src):
    # Initialize distances from src to all other vertices as infinite
    dis = [sys.maxsize] * V
    dis[src] = 0

    # Relax all edges |V| - 1 times
    for _ in range(V - 1):
        for u, v, w in graph:
            if dis[u] != sys.maxsize and dis[u] + w < dis[v]:
                dis[v] = dis[u] + w

    # Check for negative-weight cycles
    for u, v, w in graph:
        if dis[u] != sys.maxsize and dis[u] + w < dis[v]:
            print("Graph contains negative weight cycle")
            return

    # Print all distances
    print("Vertex Distance from Source")
    for i in range(V):
        print(f"{i}\t\t{dis[i]}")

def main():
    V = 5  # Number of vertices in graph
    E = 8  # Number of edges in graph

    # Every edge has three values (u, v, w) where
    # the edge is from vertex u to vertex v with weight w
    graph = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3],
    ]

    bellman_ford(graph, V, E, 0)

if __name__ == "__main__":
    main()
