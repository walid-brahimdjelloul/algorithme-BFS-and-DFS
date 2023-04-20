def dfs(graph, start_vertex, terget_vertex, visited=None):
    if visited == None:
        visited = []
    
    visited.append(start_vertex)

    if start_vertex == terget_vertex:
        return visited

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, terget_vertex, visited)
            if path:
                return path

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

test = dfs(the_most_dangerous_graph, "crocodiles", "sharks")
print(test)