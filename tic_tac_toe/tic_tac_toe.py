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
    # to do 
    pass

def show(x_cells, o_cells):
    ''' 
    -input:
    x_cells : the cells taken by 'x' player
    o_cells : the cells taken by 'o' player

    -ouput:
    prints the layout of the board shape above (doesn't return anything)
    '''
    # to do 
    pass


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
    # to do 
    return 'change this'

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