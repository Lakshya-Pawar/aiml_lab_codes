import math

def print_board(board):
    print(f"""
    {board[0]} | {board[1]} | {board[2]}
    ---+---+---
    {board[3]} | {board[4]} | {board[5]}
    ---+---+---
    {board[6]} | {board[7]} | {board[8]}
    """)

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player = 'X'
    computer = 'O'

    print("Welcome to Tic Tac Toe! You are 'X' and the AI is 'O'.")
    print_board(board)

    while True:
        if player == 'X':
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                continue
        else:
            move = best_move(board)
            print(f"AI chooses position {move + 1}")

        board[move] = player
        print_board(board)

        if check_winner(board, player):
            if player == 'X':
                print("Congratulations! You win!")
            else:
                print("AI wins! Better luck next time.")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
