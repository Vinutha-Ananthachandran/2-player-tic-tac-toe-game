game_line = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
            [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
sep_line  = '-----------'
player = {1:'',2:''}
column_mapping = {1:1,2:5,3:9}

from IPython.display import clear_output
def display_board(clear):
    '''
    prints the game board on the screen after each move
    '''
    if clear:
        clear_output()
    for index,item in enumerate(game_line):
        print(''.join(item))
        if index != 2:
            print(sep_line)

from IPython.display import clear_output
def player_pawn_selection():
    '''
    lets the player 1 and 2 choose between X and O
    '''
    while True:
        choice = (input('Player 1, do you want X or O ? ')).upper()
        if choice == 'X':
            player[1] = 'X'
            player[2] = 'O'
            clear_output()
            print(f'Player 1 is {player[1]} and Player 2 is {player[2]}')
            break
        elif choice == 'O':
            player[1] = 'O'
            player[2] = 'X'
            clear_output()
            print(f'Player 1 is {player[1]} and Player 2 is {player[2]}')
            break
        else:
            print('invalid selection. try again, Player 1')

def grid_selection(player_id):
    while True:
        row = input('Player, enter the row to be selected (1-3): ')
        col = input('Player, enter the column to be selected (1-3)')
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if 1<=row<=3 and 1<=col<=3:
                if game_line[row-1][column_mapping[col]] == ' ':
                    game_line[row-1][column_mapping[col]] = player[player_id]
                    if validate_selection():
                        return game_over(player_id)
                    break
                else:
                    print('cell not available')
            else:
                print('incorrect row number')

def validate_selection():
    '''
    check if any player has won the game
    '''
    line = []
    generate_validation_lines(line)
    for item in line:
        if str(item) == 'XXX' or str(item) == 'OOO':
            return True
    return False

def generate_validation_lines(line):
    '''
    lines for matching the tic-tac-toe grid
    '''
    line1 = ''
    line2 = ''
    line3 = ''
    for index,item in enumerate(game_line):
        line.append(str(game_line[index][1]) + str(game_line[index][5]) + str(game_line[index][9]))
        line1+=str(game_line[index][1])
        line2+=str(game_line[index][5])
        line3+=str(game_line[index][9])
    line.append(line1)
    line.append(line2)
    line.append(line3)
    line.append(str(game_line[0][1])+str(game_line[1][5])+str(game_line[2][9]))
    line.append(str(game_line[0][9])+str(game_line[1][5])+str(game_line[2][1]))

def game_over(player_id):
    '''
    terminates the game and annouces the winner
    '''
    print(f'Congratulations Player {player_id}, you WON!!')
    return True

def check_for_game_over():
    '''
    To check if all the cells of the grid is selected, if yes then the game terminates
    '''
    for index,item in enumerate(game_line):
        if game_line[index][1] == ' ' or game_line[index][5] == ' ' or game_line[index][9] == ' ':
            return False
    return True

def tic_tac_toe():
    '''
    functionality of the tic tac toe game
    '''
    print('WELCOME TO TIC TAC TOE')
    player_pawn_selection()
    while True:
        display_board(True)
        print("Player 1's Turn")
        if grid_selection(1):
            break
        if check_for_game_over():
            break
        display_board(True)
        print("Player 2's Turn")
        if grid_selection(2):
            break
        if check_for_game_over():
            break
    display_board(False)
    print("GAME OVER")
