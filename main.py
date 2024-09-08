import bfs
import dfs
import a_star
import a_star2
import time
import tracemalloc 
import pandas as pd

def read_puzzles_from_file(filename="8puzzles.txt"):
    puzzles = []
    current_puzzle = []
    
    with open(filename, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.startswith("8-Puzzle"):
                continue 
            elif stripped_line == "":
                if current_puzzle:
                    puzzles.append(current_puzzle)
                    current_puzzle = []
            else:
                row = list(map(int, stripped_line.strip('[]').split(',')))
                current_puzzle.append(row)
        if current_puzzle:  
            puzzles.append(current_puzzle)
    
    return puzzles

def run_algorithm_and_record_time(algorithm_name, search_function, initial_state, goal_state, puzzle_id, results):
    print(f"{algorithm_name} {puzzle_id}")
    
    tracemalloc.start()
    
    start_time = time.time()
    depth, nodes_generated, max_queue_size = search_function(initial_state, goal_state)
    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    elapsed_time = end_time - start_time
    print(f"Time taken for {algorithm_name} on 8-Puzzle {puzzle_id}: {elapsed_time:.4f} seconds")
    print(f"Goal state found at depth: {depth}")
    print(f"Total nodes generated: {nodes_generated}")
    print(f"Maximum queue size: {max_queue_size}")
    print(f"Peak memory usage: {peak / 1024:.2f} KB\n")  
    
    results.append((
        f"8-Puzzle {puzzle_id}",
        algorithm_name,
        elapsed_time,
        depth,
        nodes_generated,
        max_queue_size,
        peak / 1024  
    ))

def main():
    puzzles = read_puzzles_from_file("8puzzles.txt")
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    results = []

    for i, initial_state in enumerate(puzzles, 1):
        print(f"\n8-Puzzle {i}:")
        for row in initial_state:
            print(row)
        print("\n")
        
        run_algorithm_and_record_time("A* - Manhattan", a_star.search, initial_state, goal_state, i, results)
        run_algorithm_and_record_time("A* - Euclidean", a_star2.search, initial_state, goal_state, i, results)
        run_algorithm_and_record_time("BFS", bfs.search, initial_state, goal_state, i, results)
        run_algorithm_and_record_time("DFS", dfs.search, initial_state, goal_state, i, results)

    # Salvar os resultados em um arquivo Excel
    df = pd.DataFrame(results, columns=[
        "Puzzle", "Algorithm", "Time (seconds)", "Depth", "Total Nodes Generated", "Max Queue Size", "Peak Memory Usage (KB)"
    ])
    df.to_excel("8puzzle_results.xlsx", index=False)
    print("Results saved to 8puzzle_results.xlsx")

if __name__ == "__main__":
    main()
