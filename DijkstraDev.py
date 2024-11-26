import sys

# Number of vertices in the graph
V = 9

# Function to find the vertex with minimum distance value
def min_distance(distance, spt_set):
    min_val = sys.maxsize
    min_index = -1

    for i in range(V):
        if not spt_set[i] and distance[i] <= min_val:
            min_val = distance[i]
            min_index = i

    return min_index

# Function to print the solution
def print_solution(distance):
    print("Vertex\t\tDistance from Source")
    for i in range(V):
        print(f"{i}\t\t\t{distance[i]}")

# Function that implements Dijkstra's single-source shortest path algorithm
def dijkstra(graph, src):
    distance = [sys.maxsize] * V  # Initialize all distances as INFINITE
    spt_set = [False] * V  # spt_set[i] will be True if vertex i is included in shortest path tree

    # Distance of source vertex from itself is always 0
    distance[src] = 0

    for _ in range(V - 1):
        # Pick the minimum distance vertex from the set of vertices not yet processed
        u = min_distance(distance, spt_set)
        spt_set[u] = True

        # Update distance value of the adjacent vertices of the picked vertex
        for v in range(V):
            if (
                graph[u][v] > 0 and  # Check if there's an edge
                not spt_set[v] and  # Check if vertex v is not in the shortest path tree
                distance[u] != sys.maxsize and  # Ensure the distance to u is not infinite
                distance[v] > distance[u] + graph[u][v]  # Relaxation step
            ):
                distance[v] = distance[u] + graph[u][v]

    print_solution(distance)

# Driver code
if __name__ == "__main__":
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]

    dijkstra(graph, 0)
