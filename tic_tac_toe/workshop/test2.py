'''
this file contains all the functions that contribute in the making of tic tac toe 
__________ about the game __________
         1-the grid shape :
              1 | 2 | 3
             -----------
              4 | 5 | 6
             -----------
              7 | 8 | 9
       2-how to play the game :
    the player with x starts first and 
must choose a case number.
____________________________________
autour: Samuj
'''

def win_check(x_cells, o_cells, the_round):
    ''' this function checks if the player that played this round won or not
    -input:
    x_cells : the cells taken by 'x' player
    o_cells : the cells taken by 'o' player
    the_round : the round we are in 
    -ouput:
    returns True if the player won or not
    '''
    
    player_cells = x_cells if the_round%2 == 1 else o_cells

    lines   = [(1+(i*3), 2+(i*3), 3+(i*3)) for i in range(3)]
    columns = [(i, i+3 , i+6) for i in range(1,4)]
    diags   = [(1,5,9),(7,5,3)]

    win_postions = [set(position) for layout in [lines, columns, diags] for position in layout]

    for position in win_postions:
        if position.issubset(player_cells):
            player = 'x' if the_round%2 == 1 else 'o'
            show(x_cells, o_cells) 
            print(f'\n{player} wins !')
            return True 

def show(x_cells, o_cells):
    ''' 
    -input:
    x_cells : the cells taken by 'x' player
    o_cells : the cells taken by 'o' player
    -ouput:
    prints the layout of the board shape above (doesn't return anything)
    '''
     
    def charcter(x):
        if x in x_cells:
            return ' x '
        elif x in o_cells:
            return ' o '
        return '   '
    print('\n-----------\n'.join('|'.join(list(map(charcter,(1+(i*3), 2+(i*3), 3+(i*3))))) for i in range(3)))


def valid_cell(x_cells, o_cells):
    ''' this function checks if an input is valid or not, for that to be 
    true it must be a digit in range(1,10) and not included in x_cells or 
    o_cells. 
    -input:
    x_cells : the cells taken by 'x' player
    o_cells : the cells taken by 'o' player
    -ouput:
    return the valid cell entered by the user 
    '''

    while True:
        cell = input('what cell do you choose: ')
        if cell.isdigit():
            cell = int(cell)
            if not cell in x_cells and not cell in o_cells and 1 <= cell <= 9:
                print()
                return cell
            else:
                print('not available, try again !')
        else:
            print('give a valid number, try again !')
    

def tic_tac_toe():
    ''' this is the body of the game use the function above to make it work'''

    x_cells = set()
    o_cells = set()
    
    the_round = 1

    while the_round < 10:
        player = 'x' if the_round%2 == 1 else 'o'
        print(f'\nround {the_round} it is {player} to play \n')

        cell = valid_cell(x_cells, o_cells)
        if the_round % 2 == 1:
            x_cells.add(cell)
        else:
            o_cells.add(cell)
            
        if win_check(x_cells, o_cells, the_round):
            return

        show(x_cells, o_cells)        
        the_round += 1

    print('\ndraw')

if __name__ == '__main__':
    tic_tac_toe()