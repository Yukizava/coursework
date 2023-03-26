import numpy as np
import copy
matrix = [[0, 1, 2, 4, 1], [1, 0, 2, 3, 5], [2, 2, 0, 4, 5], [4, 3, 4, 0, 3], [1, 5, 5, 3, 0]]
def heuristic_algorithm(matrix):
    copy_matrix = copy.deepcopy(matrix)
    free_node = [i for i in range(0, len(matrix))]
    increment = dict() # ключ = вершина, значени = список, выбор значения и ключа, которое третье значение списка минимальна
    min_res = np.argmin(matrix, axis=0)
    min_res_column = list(min_res)[0]
    min_res_rows = list(min_res)[1]
    free_node.remove(min_res_column), free_node.remove(min_res_rows)
    result = [[min_res_column, min_res_rows], [min_res_rows, min_res_column]]
    while len(result) != len(matrix):

        break
    print(free_node)
    return result

def calculate(matrix, result, node):

    return

print(heuristic_algorithm(matrix))