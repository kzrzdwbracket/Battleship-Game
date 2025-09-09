import random

GRID_SIZE = 5  # 5x5 grid
SHIP_COUNT = 3  # number of ships

def print_grid(grid, reveal=False):
    print("  " + " ".join(str(i+1) for i in range(GRID_SIZE)))
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            cell = grid[i][j]
            if cell == "S" and not reveal:
                row.append(".")
            else:
                row.append(cell)
        print(str(i+1) + " " + " ".join(row))

def place_ships(grid):
    ships = []
    while len(ships) < SHIP_COUNT:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == ".":
            grid[x][y] = "S"
            ships.append((x, y))
    return ships

def all_ships_sunk(grid):
    for row in grid:
        if "S" in row:
            return False
    return True

def get_guess():
    while True:
        try:
            coords = input("Enter your guess (row,col, e.g. 2,3): ")
            row_str, col_str = coords.split(",")
            row = int(row_str) - 1
            col = int(col_str) - 1
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                return row, col
            else:
                print(f"Coordinates must be between 1 and {GRID_SIZE}.")
        except Exception:
            print("Invalid input. Use the format row,col (e.g. 2,3).")

def main():
    print("Welcome to Battleship!")
    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    place_ships(grid)
    turns = 0

    while not all_ships_sunk(grid):
        print_grid(grid)
        row, col = get_guess()
        turns += 1
        if grid[row][col] == "S":
            print("Hit!")
            grid[row][col] = "X"
        elif grid[row][col] == ".":
            print("Miss!")
            grid[row][col] = "O"
        elif grid[row][col] in ("X", "O"):
            print("Already guessed there.")

    print("\nCongratulations! You sank all the ships in", turns, "turns.")
    print("Final grid (S = ship, X = hit, O = miss):")
    print_grid(grid, reveal=True)

if __name__ == "__main__":
    main()
