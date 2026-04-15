def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def check_win(board, player):
    # Rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter col (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Out of range! Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()