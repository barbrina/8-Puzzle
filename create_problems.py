import random

def is_solvable(puzzle):
    flat_puzzle = [num for row in puzzle for num in row]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j] != 0:
                inversions += 1
    return inversions % 2 == 0

def generate_puzzle():
    while True:
        numbers = list(range(9))
        random.shuffle(numbers)
        puzzle = [numbers[i:i+3] for i in range(0, 9, 3)]
        if is_solvable(puzzle):
            return puzzle

def generate_multiple_puzzles(n=30):
    puzzles = []
    seen_puzzles = set()
    
    while len(puzzles) < n:
        puzzle = generate_puzzle()
        puzzle_tuple = tuple(tuple(row) for row in puzzle)
        
        if puzzle_tuple not in seen_puzzles:
            puzzles.append(puzzle)
            seen_puzzles.add(puzzle_tuple)
    
    return puzzles

def save_puzzles_to_file(puzzles, filename="8puzzles.txt"):
    with open(filename, "w") as file:
        for i, puzzle in enumerate(puzzles):
            file.write(f"8-Puzzle {i+1}:\n")
            for row in puzzle:
                file.write(f"{row}\n")
            file.write("\n")

puzzles = generate_multiple_puzzles(30)

save_puzzles_to_file(puzzles, "8puzzles.txt")

print("Puzzles saved to 8puzzles.txt")
