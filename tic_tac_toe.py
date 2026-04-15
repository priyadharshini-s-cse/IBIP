def create_board():
    return [" " for _ in range(9)]

def display_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            return True
    return False

def play_game():
    board = create_board()
    player = "X"

    for turn in range(9):
        display_board(board)

        try:
            move = int(input(f"Player {player}, enter position (0-8): "))
        except:
            print("Enter number only!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = player

        if check_winner(board, player):
            display_board(board)
            print(f"🎉 Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    display_board(board)
    print("😐 It's a Tie!")

# Play again option
while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Game Ended")
        break