from copy import deepcopy
from math import sqrt

def print_puzzle(state):
    for row in state:
        print(row)
    print("\n")


def find_position(goal, value):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return i, j


def heuristic_manhattan(state, goal):
    "Heuristic: Distancia de Manhattan para o Eight Puzzle."

    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0 and value != goal[i][j]:
                _i, _j = find_position(goal, value)
                total_distance += abs(i - _i) + abs(j - _j)
    return total_distance

def misplaced_tile_heuristic(state, goal):
    "Heuristica: conta o numero de pecas fora de lugar."
    misplaced_count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced_count += 1
    return misplaced_count

def euclidean_distance_heuristic(state, goal):
    "Heuristica: calcula a distancia euclidiana total das pecas ate suas posicoes corretas."
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                for goal_i in range(3):
                    for goal_j in range(3):
                        if goal[goal_i][goal_j] == value:
                            total_distance += sqrt((goal_i - i) ** 2 + (goal_j - j) ** 2)
                            break
    return total_distance

def find_empty_element(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def makeDescendants(state):
    descendants = []
    empty_row, empty_col = find_empty_element(
        state
    )  # used to find the row and column of the element '0'

    # Move up
    if empty_row > 0:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = (
            new_state[empty_row - 1][empty_col],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move down
    if empty_row < 2:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = (
            new_state[empty_row + 1][empty_col],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move left
    if empty_col > 0:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = (
            new_state[empty_row][empty_col - 1],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move right
    if empty_col < 2:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = (
            new_state[empty_row][empty_col + 1],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    return descendants