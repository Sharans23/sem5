import sys

V=9

def min_dist(dist,spt_set):
    min_val=sys.maxsize
    min_index=-1
    
    for v in range(V):
        if not spt_set[v] and dist[v]<=min_val:
            min_val=dist[v]
            min_index=v
    return min_index        

def dijkstra(graph,source):
    dist=[sys.maxsize]*V
    spt_set=[False]*V
    
    dist[source]=0
    
    for _ in range(V-1):
        u=min_dist(dist,spt_set)
        spt_set[u]=True
        
        for v in range(V):
            if(not spt_set[v] and graph[u][v] and dist[u]!=sys.maxsize and dist[u]+graph[u][v]<dist[v]):
                dist[v]=dist[u]+graph[u][v]

    for i in range(V):
        print(f'{i}\t\t{dist[i]}')     
    
    
def main():
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
                
main()                