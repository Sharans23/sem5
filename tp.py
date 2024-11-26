import sys
V=9

def dijkstras(graph,src):
    dist=[sys.maxsize]*V
    dist[src]=0
    src_set=[False]*V
    
    for _ in range(V-1):
        u=min_dist(dist,src_set)
        src_set[u]=True
        
        for v in range(V):
            if(not src_set[v] and dist[u]!=sys.maxsize and graph[u][v] and dist[u]+graph[u][v]<dist[v]):
                dist[v]=graph[u][v]+dist[u]
        
    for i in range(V):
        print(f'{i}\t\t{dist[i]}')  
        
def min_dist(dist,src_set):
    min_index=-1
    min_val=sys.maxsize
    
    for v in range(V):
        if(not src_set[v] and dist[v]<min_val):
            min_val=dist[v]
            min_index=v
    return min_index
    
def main():
    graph=[
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    dijkstras(graph,0)
    
main()    