import pygame, sys, os 

SCREEN_SIZE  = (400, 500)
SCREEN_COLOR = pygame.Color('#FFFFFF')
GAME_FRAMES  = {i:pygame.image.load(os.path.join('frames', f'{i}.png')) for i in 'X,O,E,grid,Draw,X_WIN,O to play,X to play,reset,title,X wins,O wins'.split(',')}
CASE_WIDTH   = 100

'''
 1 | o | 3
___________
 4 | x | 6
___________
 7 | 8 | 9
'''
class Game_functions():
    def __init__(self):
        self.x_cells   = set()
        self.o_cells   = set()
        self.the_round = 1
        self.ended     = False
        self.win_pos   = []

    def win_check(self):
        ''' this function checks if the player that played this round won or not
        -ouput:
        returns True if the player won or not
        '''
        
        player_cells = self.x_cells if self.the_round%2 == 1 else self.o_cells

        lines   = [(1+(i*3), 2+(i*3), 3+(i*3)) for i in range(3)]
        columns = [(i, i+3 , i+6) for i in range(1,4)]
        diags   = [(1,5,9),(7,5,3)]

        win_postions = [set(position) for layout in [lines, columns, diags] for position in layout]

        for position in win_postions:
            if position.issubset(player_cells):
                player = 'X' if self.the_round%2 == 1 else 'O'
                self.ended = True 
                self.win_pos = position
                return f'{player} wins'

        if self.the_round == 9:
            self.ended = True 
            return 'Draw'

class Game():
    def __init__(self):
        self.win = 'draw'

    def turn(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()     
            if event.type == pygame.MOUSEBUTTONDOWN:
                n,m = pygame.mouse.get_pos()
                if 300 <= n <= 430 and 439 <= m <= 489:
                    self.play()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                n,m = pygame.mouse.get_pos()
                n = (n-50)//CASE_WIDTH
                m = (m-125)//CASE_WIDTH
                x = m*3 + n + 1
                if 0 <= n < 3 and 0 <= m < 3 and (not x in self.game.x_cells and not x in self.game.o_cells):
                    if self.game.the_round%2 == 1:
                        self.game.x_cells.add(x)
                    else:
                        self.game.o_cells.add(x)
                    self.win = self.game.win_check()
                    self.game.the_round += 1
    
    def update(self, screen):
        def frames(x):
            if x in self.game.x_cells:
                return 'X'
            elif x in self.game.o_cells:
                return 'O'
            else:
                return 'E'

        screen.fill(SCREEN_COLOR)
        screen.blit(GAME_FRAMES['title'], (106, 24)) 
        screen.blit(GAME_FRAMES['grid'], (50, 125))  
        screen.blit(GAME_FRAMES['reset'], (301,439))

        for i in range(3):
            for j in range(3):
                x = i*3 + j + 1
                screen.blit(GAME_FRAMES[frames(x)], (50 + j*CASE_WIDTH, 125 + i*CASE_WIDTH))

        if self.game.ended:
            screen.blit(GAME_FRAMES[self.win], (50, 455))
            if self.win == 'X wins':
                for i in self.game.win_pos:
                    x,y = (i-1)%3, (i-1)//3
                    screen.blit(GAME_FRAMES['X_WIN'], (50 + x*CASE_WIDTH, 125 + y*CASE_WIDTH))
            self.game_over()

        pygame.display.flip()

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                n,m = pygame.mouse.get_pos()
                if 300 <= n <= 430 and 439 <= m <= 489:
                    self.play() 

    def play(self):
        # start pygame
        self.game = Game_functions()
        pygame.init() 
        pygame.display.set_caption('tic tac toe')
        screen = pygame.display.set_mode(SCREEN_SIZE)

        while True:
            self.turn()
            self.update(screen)

if __name__ == '__main__':
    game = Game() 
    game.play()