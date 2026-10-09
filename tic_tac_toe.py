import random

# Create board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Display board
def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check_win(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

# Main game
while True:

    show_board()

    # User move
    move = int(input("Enter your position (1-9): "))

    if board[move-1] == "X" or board[move-1] == "O":
        print("Position already taken! Try again.")
        continue

    board[move-1] = "X"

    if check_win("X"):
        show_board()
        print("🎉 You Win!")
        break

    # Check draw
    if "1" not in board and "2" not in board and "3" not in board and \
       "4" not in board and "5" not in board and "6" not in board and \
       "7" not in board and "8" not in board and "9" not in board:
        show_board()
        print("🤝 Match Draw!")
        break

    # Computer move
    empty = []

    for i in range(9):
        if board[i] not in ["X", "O"]:
            empty.append(i)

    computer = random.choice(empty)
    board[computer] = "O"

    print("Computer chose:", computer + 1)

    if check_win("O"):
        show_board()
        print("💻 Computer Wins!")
        break
