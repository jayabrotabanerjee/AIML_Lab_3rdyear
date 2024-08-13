import uuid

def get_mac_address():
    """Retrieve the MAC address of the machine."""
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0, 2*6, 2)][::-1])
    return mac

def print_board(board):
    """Print the Tic Tac Toe board."""
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    -----------
     {board[3]} | {board[4]} | {board[5]}
    -----------
     {board[6]} | {board[7]} | {board[8]}
    """)

def check_win(board, player):
    """Check if the given player has won."""
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6]   # Diagonal top-right to bottom-left
    ]
    
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def check_draw(board):
    """Check if the game is a draw (no empty spaces left)."""
    return all(space in ['X', 'O'] for space in board)

def get_move(player):
    """Get a valid move from the player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Move must be between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the Tic Tac Toe game."""
    board = [' ' for _ in range(9)]  # Initialize the board
    current_player = 'X'
    
    while True:
        print_board(board)
        move = get_move(current_player)
        
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("The space is already occupied. Try again.")
            continue
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Print the MAC address
    mac_address = get_mac_address()
    print(f"\nMAC Address: {mac_address}")

if __name__ == "__main__":
    main()

