import pygame, sys, os

SCREEN_SIZE  = (400, 500)
SCREEN_COLOR = pygame.Color('#FFFFFF')
GAME_FRAMES  = {i:pygame.image.load(os.path.join('frames', f'{i}.png')) for i in 'X,O,E,grid,Draw,O to play,X to play,reset,title,X wins,O wins'.split(',')}
CASE_WIDTH   = 100

pygame.init() 
pygame.display.set_caption('test')
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.blit(GAME_FRAMES['O'],(50,50))
x,y = (50,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -= 5          
            if event.key == pygame.K_UP:
                y -= 5            
            if event.key == pygame.K_DOWN:
                y += 5

        screen.fill(SCREEN_COLOR)   
        screen.blit(GAME_FRAMES['O'],(x,y))                
        pygame.display.flip()
