def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for tuple in ancestors:
        for vertex in tuple:
            if vertex not in graph:
                graph[vertex] = set()
        graph[tuple[1]].add(tuple[0])

    if len(graph[starting_node]) == 0:
        return -1
    holdinglist = [starting_node]
    holdinglist2 = []
    candidates = []
    while True:
        flag = False
        for element in holdinglist:
            if len(graph[element]) == 0:
                candidates.append(element)
            else:
                flag = True
                for vertex in graph[element]:
                    holdinglist2.append(vertex)
        if flag == False:
            return min(candidates)
        else:
            holdinglist = holdinglist2[:]
            holdinglist2.clear()
            candidates.clear()
