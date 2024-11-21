# board.py

# Define the board with regions
board = [
    [0, 0, 1, 1, 2],  # Each number represents a region
    [0, 3, 3, 2, 2],
    [4, 3, 3, 2, 5],
    [4, 4, 3, 5, 5],
    [6, 6, 6, 5, 5]
]

# Define the initial state of each cell
state = [[0] * 5 for _ in range(5)]  # 0 = empty, 1 = queen, -1 = blocked (X)

def print_board():
    for row in state:
        print(" ".join(str(x) for x in row))