def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    queue = [vertex_and_path]
    visited = set()

    while queue:
        current_vertex, path = queue.pop(0)
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]
                else:
                    queue.append([neighbor, (path+[neighbor])])

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

test = bfs(the_most_dangerous_graph, 'crocodiles', 'bees')
print(test)