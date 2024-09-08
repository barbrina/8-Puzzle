from collections import deque
from utils import makeDescendants, print_puzzle

def search(initial_state, goal_state):
    stack = deque([(initial_state, 0)])  # Pilha de estados a serem explorados
    explored = set()  # Conjunto de estados já explorados
    total_nodes_generated = 0  # Contador de nós gerados
    max_stack_size = 1  # Tamanho máximo da pilha

    while stack:
        current_state, depth = stack.pop()
        total_nodes_generated += 1
        max_stack_size = max(max_stack_size, len(stack))

        if current_state == goal_state:
            return depth, total_nodes_generated, max_stack_size

        explored.add(tuple(map(tuple, current_state)))
        descendants = makeDescendants(current_state)

        for descendant in reversed(descendants):  # Reverso para manter a ordem LIFO
            descendant_tuple = tuple(map(tuple, descendant))
            if descendant_tuple not in explored:
                stack.append((descendant, depth + 1))

    print("\nNo result found")
    return None, total_nodes_generated, max_stack_size  # Retorna None se não encontrar solução
