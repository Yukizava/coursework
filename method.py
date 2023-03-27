import numpy as np
matrix_for_test = [[0, 1, 2, 4, 1], [1, 0, 2, 3, 5], [2, 2, 0, 4, 5], [4, 3, 4, 0, 3], [1, 5, 5, 3, 0]]


def heuristic_algorithm(matrix):
    free_node = [i for i in range(0, len(matrix))]
    increment = dict()
    min_res = np.argmin(matrix, axis=0)
    min_res_column = list(min_res)[0]
    min_res_rows = list(min_res)[1]
    free_node.remove(min_res_column), free_node.remove(min_res_rows)
    result = [[min_res_column, min_res_rows], [min_res_rows, min_res_column]]
    while len(result) != len(matrix):
        print(result)
        for node in free_node:
            increment[node] = calculate(matrix, result, node)
        new_node_in_cycle = get_min_node(increment)
        free_node.remove(new_node_in_cycle)
        private_solution = increment.get(new_node_in_cycle)
        result.remove([private_solution[0][0], private_solution[1][1]])
        result.append(private_solution[0])
        result.append(private_solution[1])
        increment.clear()
    max_length = -1
    excess = None
    for edge in result:
        if matrix[edge[0]][edge[1]] > max_length:
            max_length = matrix[edge[0]][edge[1]]
            excess = edge
    result.remove(excess)
    save_sum = get_sum_solution(matrix, result)
    result = get_result(result)
    return result, save_sum


def calculate(matrix, result, node):
    top_edge = result[0]
    inc = float("inf")
    for edge in result:
        if matrix[edge[0]][node] + matrix[node][edge[1]] < inc:
            top_edge = edge
            inc = matrix[edge[0]][node] + matrix[node][edge[1]]
    return [[top_edge[0], node], [node, top_edge[1]], inc]


def get_min_node(increment):
    min_inc = float("inf")
    top_key = None
    for key in increment.keys():
        if increment.get(key)[2] <= min_inc:
            min_inc = increment.get(key)[2]
            top_key = key
    return top_key


def get_sum_solution(matrix, result):
    sum = 0
    for edge in result:
        sum += matrix[edge[0]][edge[1]]
    return sum


def get_result(result):
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] += 1
    return result


print(heuristic_algorithm(matrix_for_test))