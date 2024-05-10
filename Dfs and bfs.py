Graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]  
}

def bfs(visited, queue, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=' ')
        
        for neighbour in Graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            
visited=[]
queue=[]
bfs(visited,queue,'5')


graph={
   '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]  
}

visited=set()

def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(graph,visited,neighbour)

node="5"
dfs(graph,visited,node)
        