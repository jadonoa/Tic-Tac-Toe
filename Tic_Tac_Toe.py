import random


# prints out a representation of the board to the console
def show_board(b):
    print(' ')
    print('     |     |')
    print('  ' + b[0] + '  |  ' + b[1] + '  |  ' + b[2])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[3] + '  |  ' + b[4] + '  |  ' + b[5])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[6] + '  |  ' + b[7] + '  |  ' + b[8])
    print('     |     |')
    print(' ')


# check if player has won in any of the 8 possible ways
def check_win(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # Top Horizontal Win
            (b[3] == m and b[4] == m and b[5] == m) or  # Middle Horizontal Win
            (b[6] == m and b[7] == m and b[8] == m) or  # Bottom Horizontal Win
            (b[0] == m and b[3] == m and b[6] == m) or  # Left Vertical Win
            (b[1] == m and b[4] == m and b[7] == m) or  # Middle Vertical Win
            (b[2] == m and b[5] == m and b[8] == m) or  # Right Vertical Win
            (b[0] == m and b[4] == m and b[8] == m) or  # Left-to-Right Diagonal Win
            (b[2] == m and b[4] == m and b[6] == m))    # Right-to-Left Diagonal Win


# check if there is a draw after checking for a win
def check_draw(b):
    return ' ' not in b


def get_computer_move_easy(b):
    # check computer win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'X', i):
            return i

    # check player win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'O', i):
            return i

    # play a random corner
    corners = [0, 2, 6, 8]
    picking = True
    while picking:
        i = random.choice(corners)
        if b[i] == ' ':
            return i
        else:
            corners.remove(i)

        if not corners:
            picking = False

    # # play a corner
    # for i in [0, 2, 6, 8]:
    #     if b[i] == ' ':
    #         return i

    # play the center
    if b[4] == ' ':
        return 4

    # play a random side
    sides = [1, 3, 5, 7]
    picking = True
    while picking:
        i = random.choice(sides)
        if b[i] == ' ':
            return i
        else:
            sides.remove(i)

        if not sides:
            picking = False

    # # play a side
    # for i in [1, 3, 5, 7]:
    #     if b[i] == ' ':
    #         return i


def get_computer_move_medium(b):

    # check computer win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'X', i):
            return i

    # check player win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'O', i):
            return i

    # check computer for fork opportunities
    for i in range(0, len(b)):
        if b[i] == ' ' and test_for_fork(b, 'X', i):
            return i

    # check player for fork opportunities
    for i in range(0, len(b)):
        if b[i] == ' ' and test_for_fork(b, 'O', i):
            return i

    # play a random corner
    corners = [0, 2, 6, 8]
    picking = True
    while picking:
        i = random.choice(corners)
        if b[i] == ' ':
            return i
        else:
            corners.remove(i)

        if not corners:
            picking = False

    # play the center
    if b[4] == ' ':
        return 4

    # play a random side
    sides = [1, 3, 5, 7]
    picking = True
    while picking:
        i = random.choice(sides)
        if b[i] == ' ':
            return i
        else:
            sides.remove(i)

        if not sides:
            picking = False


def get_computer_move_hard(b):

    # check computer win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'X', i):
            return i

    # check player win moves
    for i in range(0, len(b)):
        if b[i] == ' ' and test_win_move(b, 'O', i):
            return i

    # check computer for fork opportunities
    for i in range(0, len(b)):
        if b[i] == ' ' and test_for_fork(b, 'X', i):
            return i

    # check player for fork opportunities and block with a side move if there are two forks
    player_forks = 0
    for i in range(0, len(b)):
        if b[i] == ' ' and test_for_fork(b, 'O', i):
            player_forks += 1
            temp_move = i

    if player_forks == 1:
        return temp_move
    elif player_forks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j

        # play the center
    if b[4] == ' ':
        return 4

    # play a random corner
    corners = [0, 2, 6, 8]
    picking = True
    while picking:
        i = random.choice(corners)
        if b[i] == ' ':
            return i
        else:
            corners.remove(i)

        if not corners:
            picking = False

    # play a random side
    sides = [1, 3, 5, 7]
    picking = True
    while picking:
        i = random.choice(sides)
        if b[i] == ' ':
            return i
        else:
            sides.remove(i)

        if not sides:
            picking = False


def get_board_copy(b):
    # get a duplicate of the board so we don't change actual moves
    duplicate_b = []
    for i in b:
        duplicate_b.append(i)
    return duplicate_b


def test_win_move(b, mark, i):
    # b is the board
    # mark is either 'X' or 'O'
    # i is the desired move
    board_copy = get_board_copy(b)
    board_copy[i] = mark
    return check_win(board_copy, mark)


def test_for_fork(b, mark, i):
    # tests whether a move opens up a fork

    # b is the board
    # mark is either 'X' or 'O'
    # i is the desired move

    board_copy = get_board_copy(b)
    board_copy[i] = mark
    winning_moves = 0
    for j in range(0, len(b)):
        if test_win_move(board_copy, mark, j) and board_copy[j] == ' ':
            winning_moves += 1
    return winning_moves >= 2


def single_player(in_game, b):
    setting_up = True
    while setting_up:
        print(" ")
        print("Pick Difficulty:")
        print(" ")
        print("(1)Easy             (2)Medium             (3)Hard")
        difficulty = input()

        if difficulty != '1' and difficulty != '2' and difficulty != '3':
            print(" ")
            print("INVALID DIFFICULTY!")
            continue

        print(" ")
        print("Do you want to go (1)First or (2)Second? (HINT: Second is harder)")
        f_or_s = input()
        if f_or_s != '1' and f_or_s != '2':
            print(" ")
            print("INVALID CHOICE!")
            continue

        if f_or_s == '1':
            player_marker = 'O'
            show_board(b)
        else:
            player_marker = 'X'

        setting_up = False

    while in_game:
        # player 1 goes first
        if player_marker == 'O':
            print('Your Move: (0-8)')
            move = int(input())
            # move is invalid if the space on the board is not empty
            if b[move] != ' ':
                print("INVALID MOVE!")
                continue
        # if the user has chosen to be player 2 then the computer goes first
        else:
            if difficulty == '1':
                move = get_computer_move_easy(b)
            elif difficulty == '2':
                move = get_computer_move_medium(b)
            else:
                move = get_computer_move_hard(b)

        b[move] = player_marker
        # check if there is a win
        if check_win(b, player_marker):
            in_game = False
            show_board(b)
            if player_marker == 'O':
                print("PLAYER 1 WINS!")
                print(' ')
            else:
                print("COMPUTER WINS!")
                print(' ')
            continue
        # check if there is a draw
        if check_draw(b):
            in_game = False
            show_board(b)
            print("DRAW!")
            print(' ')
            continue
        show_board(b)
        # change the player marker for next players turn
        if player_marker == 'O':
            player_marker = 'X'
        else:
            player_marker = 'O'


def two_player(in_game, b):
    show_board(b)
    player_marker = 'O'

    while in_game:
        # player 1 goes first
        if player_marker == 'O':
            print('Player 1 Move: (0-8)')
        else:
            print('Player 2 Move: (0-8)')
        move = int(input())
        # move is invalid if the space on the board is not empty
        if b[move] != ' ':
            print("INVALID MOVE!")
            continue

        b[move] = player_marker
        # check if there is a win
        if check_win(b, player_marker):
            in_game = False
            show_board(b)
            if player_marker == 'O':
                print("PLAYER 1 WINS!")
                print(' ')
            else:
                print("PLAYER 2 WINS!")
                print(' ')
            continue
        # check if there is a draw
        if check_draw(b):
            in_game = False
            show_board(b)
            print("DRAW!")
            print(' ')
            continue
        show_board(b)
        # change the player marker for next players turn
        if player_marker == 'O':
            player_marker = 'X'
        else:
            player_marker = 'O'


def play():
    playing = True
    while playing:
        # set up the game
        in_game = True
        choosing_game_mode = True
        board = [' '] * 9

        while choosing_game_mode:
            print(" ")
            print("Choose Game Mode. (1)Single Player or (2)Two Player?")
            inp = input()

            if inp != '2' and inp != '1':
                print("INVALID GAME MODE!")
                continue
            else:
                if inp == '1':
                    single_player(in_game, board)
                else:
                    two_player(in_game, board)
                choosing_game_mode = False

        print('Type y to keep playing')
        inp = input()
        if inp != 'y' and inp != 'Y':
            playing = False

    print("Thanks For Playing My Game!")


# play()
