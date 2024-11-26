import sys

V = 9  # Number of vertices in the graph

def min_distance(dist, spt_set):
    """Find the vertex with the minimum distance value from the set of vertices
    not yet included in the shortest path tree."""
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if not spt_set[v] and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v

    return min_index

def print_solution(dist):
    """Print the distance array."""
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t {dist[i]}")

def dijkstra(graph, src):
    """Implement Dijkstra's algorithm for a graph represented using an adjacency matrix."""
    dist = [sys.maxsize] * V  # Initialize distances as infinite
    spt_set = [False] * V     # Shortest path tree set

    dist[src] = 0  # Distance from the source to itself is always 0

    for _ in range(V - 1):
        u = min_distance(dist, spt_set)  # Pick the minimum distance vertex
        spt_set[u] = True  # Mark the vertex as processed

        # Update the distance of the adjacent vertices of the picked vertex
        for v in range(V):
            if (not spt_set[v] and graph[u][v] and
                dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)

if __name__ == "__main__":
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    
    dijkstra(graph, 0)
