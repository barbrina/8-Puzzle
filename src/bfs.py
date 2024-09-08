from collections import deque
from utils import makeDescendants, print_puzzle

def search(initial_state, goal_state):
    queue = deque([initial_state])
    explored = set()
    total_nodes_generated = 0 
    max_queue_size = 1  

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

    print("\nNenhum resultado encontrado.")
    return None, total_nodes_generated, max_queue_size 
