from Tic_Tac_Toe import *
import random

board = [' '] * 9
moves = list(range(0, 9))
in_game = True
player_marker = 'O'
difficulty = 'easy'
player_wins = 0
computer_wins = 0
draws = 0


for k in range(0, 2):
    if k > 0:
        player_marker = 'X'
    if player_marker == 'O':
        who_goes_first = 'Player'
    else:
        who_goes_first = 'Computer'

    difficulty = 'easy'

    for j in range(0, 3):
        if j == 1:
            difficulty = 'medium'
        elif j == 2:
            difficulty = 'hard'

        for i in range(0, 10000):
            board = [' '] * 9
            in_game = True
            while in_game:
                # player 1 goes first
                if player_marker == 'O':
                    move = random.choice(moves)
                    # move = get_computer_move_easy(board)
                    # choose another random move if the space on the board is not empty
                    if board[move] != ' ':
                        continue
                # if the user has chosen to be player 2 then the computer goes first
                else:
                    if difficulty == 'easy':
                        move = get_computer_move_easy(board)
                    elif difficulty == 'medium':
                        move = get_computer_move_medium(board)
                    else:
                        move = get_computer_move_hard(board)

                board[move] = player_marker

                # check if there is a win
                if check_win(board, player_marker):
                    in_game = False
                    # show_board(b)
                    if player_marker == 'O':
                        # print("PLAYER 1 WINS!")
                        # print(' ')
                        player_wins += 1
                    else:
                        # print("COMPUTER WINS!")
                        # print(' ')
                        computer_wins += 1
                    continue
                # check if there is a draw
                if check_draw(board):
                    in_game = False
                    # show_board(b)
                    # print("DRAW!")
                    # print(' ')
                    draws += 1
                    continue
                # show_board(b)
                # change the player marker for next players turn
                if player_marker == 'O':
                    player_marker = 'X'
                else:
                    player_marker = 'O'

        print(' ')
        print('PLAYER WINS: ', player_wins)
        print('COMPUTER WINS: ', computer_wins)
        print('DRAWS: ', draws)
        print('DIFFICULTY: ', difficulty)
        print('FIRST MOVE BY: ', who_goes_first)
        print(' ')
        player_wins = 0
        computer_wins = 0
        draws = 0

