import random

def display_board(board):
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("|", " " * 2, board[1], " " * 2, "|", " " * 2, board[2], " " * 2, "|", " " * 2, board[3], " " * 2, "|")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("|", " " * 2, board[4]," " * 2, "|", " " * 2, board[5]," " * 2, "|", " " * 2, board[6]," " * 2, "|")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("|", " " * 2, board[7]," " * 2, "|", " " * 2, board[8]," " * 2, "|", " " * 2, board[9]," " * 2, "|")
    print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+")


def check_win(board, symbol):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
        [1, 5, 9], [3, 5, 7]              # diagonal
    ]
    for combination in winning_combinations:
        if all(board[pos] == symbol for pos in combination):
            return True
    return False

def make_move(board, symbol, position):
    board[position] = symbol

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def player_move(board):
    while True:
        position = int(input("Ваш хід (введіть число від 1 до 9): "))
        if position in range(1, 10) and board[position] == str(position):
            return position
        else:
            print("Некоректний хід. Спробуйте ще раз.")

def computer_move(board):
    empty_positions = [pos for pos, cell in enumerate(board) if cell == str(pos)]
    return random.choice(empty_positions)

def play_game():
    board = [' '] + [str(i) for i in range(1, 10)]
    board[5] = 'X'  # Перший хід завжди в середину дошки

    while True:
        display_board(board)

        if check_win(board, 'X'):
            print("Комп'ютер переміг! Ви програли.")
            break
        elif check_win(board, 'O'):
            print("Вітаємо! Ви перемогли комп'ютер.")
            break
        elif is_board_full(board):
            print("Гра закінчилася внічию.")
            break

        position = player_move(board)
        make_move(board, 'O', position)

        if check_win(board, 'O'):
            display_board(board)
            print("Вітаємо! Ви перемогли комп'ютер.")
            break
        elif is_board_full(board):
            display_board(board)
            print("Гра закінчилася внічию.")
            break

        computer_position = computer_move(board)
        make_move(board, 'X', computer_position)

play_game()