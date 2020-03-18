from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for tuple in ancestors:
        for vertex in tuple:
            if vertex not in g.vertices:
                g.add_vertex(vertex)
        g.add_edge(tuple[1], tuple[0])

    if not g.vertices[starting_node]:
        return -1
    holdinglist = [starting_node]
    holdinglist2 = []
    candidates = []
    while True:
        flag = False
        for element in holdinglist:
            if not g.vertices[element]:
                candidates.append(element)
            else:
                flag = True
                for vertex in g.vertices[element]:
                    holdinglist2.append(vertex)
        if flag == False:
            return min(candidates)
        else:
            holdinglist = holdinglist2[:]
            holdinglist2.clear()
            candidates.clear()

#
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 11))
