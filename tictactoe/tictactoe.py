def print_grid(cells):
    print("---------")
    for i in range(0, 9, 3):
        row = [c if c != "_" else " " for c in cells[i:i + 3]]
        print("|", row[0], row[1], row[2], "|")
    print("---------")
def get_state(cells):
    grid = [cells[i:i + 3] for i in range(0, 9, 3)]
    lines = []
    lines.extend(grid)
    lines.extend([[grid[r][c] for r in range(3)] for c in range(3)])
    lines.append([grid[i][i] for i in range(3)])
    lines.append([grid[i][2 - i] for i in range(3)])
    x_wins = ["X", "X", "X"] in lines
    o_wins = ["O", "O", "O"] in lines
    diff = abs(cells.count("X") - cells.count("O"))
    if (x_wins and o_wins) or diff >= 2:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if "_" in cells:
        return "Game not finished"
    return "Draw"
def main():
    cells = ["_"] * 9
    player = "X"
    print_grid(cells)
    while True:
        coords = input("Enter the coordinates: ").split()
        if len(coords) != 2 or not all(c.lstrip("-").isdigit() for c in coords):
            print("You should enter numbers!")
            continue
        row, col = int(coords[0]), int(coords[1])
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        index = (row - 1) * 3 + (col - 1)
        if cells[index] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        cells[index] = player
        print_grid(cells)
        state = get_state(cells)
        if state != "Game not finished":
            print(state)
            break
        player = "O" if player == "X" else "X"
main()