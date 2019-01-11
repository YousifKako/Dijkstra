import networkx


def dijkstra(graph, start_node):
    visited = []
    lowest_value = 200
    key_of_lowest_value = 0
    map = dict()
    map[start_node] = [0, 0]

    for i in graph.nodes.keys():
        if i != start_node:
            map[i] = [100, 0]

    while len(visited) != 8:
        for i in graph.nodes:
            if map[i][0] < lowest_value and i not in visited:
                lowest_value = map[i][0]
                for key, value in map.items():
                    if value[0] == lowest_value:
                        key_of_lowest_value = key

        adj = graph.adj[key_of_lowest_value]

        for i in adj.keys():
            # print(i, "weight:", adj[i]['weight'])
            weight = adj[i]['weight']

            if weight < map[i][0]:
                key = map[i][1] = key_of_lowest_value
                key_weight = map.get(key)[0]

                if weight + key_weight < map[i][0]:
                    map[i][0] = weight + key_weight
        visited.append(key_of_lowest_value)
        lowest_value = 200
    for i, j in map.items():
        print("{}: {}".format(i, j[0]))


def main():
    graph = networkx.Graph()

    graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    graph.add_edge('A', 'B', weight=4)
    graph.add_edge('A', 'C', weight=3)
    graph.add_edge('A', 'E', weight=7)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('B', 'D', weight=5)
    graph.add_edge('E', 'D', weight=2)
    graph.add_edge('E', 'G', weight=5)
    graph.add_edge('G', 'D', weight=10)
    graph.add_edge('G', 'F', weight=3)
    graph.add_edge('D', 'F', weight=2)

    dijkstra(graph, 'A')


if __name__ == "__main__":
    main()
