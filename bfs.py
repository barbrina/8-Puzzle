from collections import deque
from utils import makeDescendants, print_puzzle

def search(initial_state, goal_state):
    queue = deque([initial_state])  # Fila de estados a serem explorados
    explored = set()  # Conjunto de estados já explorados
    total_nodes_generated = 0  # Contador de nós gerados
    max_queue_size = 1  # Tamanho máximo da fila

    # Dicionário para mapear cada estado ao seu nível de profundidade
    state_depth = {tuple(map(tuple, initial_state)): 0}

    while queue:
        current_state = queue.popleft()
        current_state_tuple = tuple(map(tuple, current_state))
        depth = state_depth[current_state_tuple]

        total_nodes_generated += 1
        max_queue_size = max(max_queue_size, len(queue))

        if current_state == goal_state:
            return depth, total_nodes_generated, max_queue_size

        explored.add(current_state_tuple)
        descendants = makeDescendants(current_state)

        for descendant in descendants:
            descendant_tuple = tuple(map(tuple, descendant))
            if descendant_tuple not in explored and descendant_tuple not in state_depth:
                queue.append(descendant)
                state_depth[descendant_tuple] = depth + 1

    print("\nNo result found")
    return None, total_nodes_generated, max_queue_size  # Retorna None se não encontrar solução
