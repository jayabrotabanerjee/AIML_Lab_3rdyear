import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()  # For spacing

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in get_available_moves(board):
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

def computer_move(board):
    move = random.choice(get_available_moves(board))
    board[move] = 'O'
    print("Computer's move:")
    print_board(board)

def main():
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == 'X':
            player_move(board)
            print_board(board)
        else:
            computer_move(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        elif ' ' not in board:
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
