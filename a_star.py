from math import sqrt


maze_map = {
    'A': {'adjacent': [('B', 5)], 'point': (1, 1)},
    'B': {'adjacent': [('A', 5), ('C', 7), ('F', 2)], 'point': (1, 6)},
    'C': {'adjacent': [('B', 7), ('L', 8)], 'point': (1, 13)},
    'D': {'adjacent': [('E', 3)], 'point': (3, 1)},
    'E': {'adjacent': [('D', 3), ('I', 6)], 'point': (3, 4)},
    'F': {'adjacent': [('B', 2), ('G', 5), ('J', 6)], 'point': (3, 6)},
    'G': {'adjacent': [('F', 5), ('K', 6)], 'point': (3, 11)},
    'H': {'adjacent': [('I', 3)], 'point': (9, 1)},
    'I': {'adjacent': [('E', 6), ('J', 2)], 'point': (9, 4)},
    'J': {'adjacent': [('F', 6), ('I', 2), ('K', 5), ('O', 2)], 'point': (9, 6)},
    'K': {'adjacent': [('G', 6), ('J', 5), ('L', 2), ('T', 9)], 'point': (9, 11)},
    'L': {'adjacent': [('C', 8), ('K', 2), ('U', 9)], 'point': (9, 13)},
    'M': {'adjacent': [('N', 3)], 'point': (11, 1)},
    'N': {'adjacent': [('M', 3), ('O', 2), ('R', 7)], 'point': (11, 4)},
    'O': {'adjacent': [('J', 2), ('N', 2), ('P', 3)], 'point': (11, 6)},
    'P': {'adjacent': [('O', 3), ('S', 7)], 'point': (11, 9)},
    'Q': {'adjacent': [('R', 3)], 'point': (18, 1)},
    'R': {'adjacent': [('N', 7), ('Q', 3), ('S', 5)], 'point': (18, 4)},
    'S': {'adjacent': [('P', 7), ('R', 5), ('T', 2)], 'point': (18, 9)},
    'T': {'adjacent': [('K', 9), ('S', 2), ('U', 2)], 'point': (18, 11)},
    'U': {'adjacent': [('L', 9), ('T', 2)], 'point': (18, 13)}
}


# count_cost = 0
result = []


def search(graph, begin_node, end_node):
    result.append(begin_node)
    count_cost = 0

    lowest_adjacent = choose_lowest_adjacent(
        graph, begin_node, end_node, result
    )

    count_cost += lowest_adjacent[1]
    result.append(lowest_adjacent[0])

    while (lowest_adjacent[0] != end_node):
        lowest_adjacent = choose_lowest_adjacent(
            graph, lowest_adjacent[0], end_node, result
        )

        count_cost += lowest_adjacent[1]
        result.append(lowest_adjacent[0])

    return (result, count_cost)


def get_heuristic(current_point, goal_point):
    x = pow(goal_point[0] - (current_point[0]), 2)
    y = pow(goal_point[1] - (current_point[1]), 2)

    return round(sqrt(x + y), 2)


def choose_lowest_adjacent(graph, current_node, goal_node, visited):
    adjacents = graph[current_node]['adjacent']
    adjacents_cost = []

    # check if the goal_node is an adjacent
    node_indicators = [node[0] for node in adjacents]

    if goal_node in node_indicators:
        adjacent = [node for node in adjacents if node[0] == goal_node][0]
        path_cost = adjacent[1]
        heuristic = get_heuristic(
            graph[goal_node]['point'], graph[current_node]['point']
        )

        return (goal_node, path_cost + heuristic)

    for adjacent in adjacents:
        if adjacent[0] not in visited and not is_dead_end(graph, adjacent[0]):
            path_cost = adjacent[1]
            heuristc = get_heuristic(
                graph[adjacent[0]]['point'], graph[goal_node]['point']
            )

            adjacents_cost.append((adjacent[0], path_cost + heuristc))

    return min(adjacents_cost, key=lambda tup: tup[1])


def is_dead_end(graph, current_adjacent):
    return (len(graph[current_adjacent]['adjacent']) == 1)


print(search(maze_map, 'A', 'Q'))
