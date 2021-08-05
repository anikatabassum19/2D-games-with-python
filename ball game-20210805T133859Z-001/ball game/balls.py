import random
import pygame
from pygame.locals import *
import sys

pygame.init()

FPS = 32
screenwidth = 600
screenheight = 400
gameDisplay = pygame.display.set_mode((screenwidth,screenheight))
ground_y = screenheight * 0.8
game_sprites = {}
game_sound = {}
PLAYER = "ball.jpg"
BACKGROUND = 'road1.jpg'
PIPE = 'stick.jpg'
intro_image = pygame.image.load('message1.jpg')
button_image = pygame.image.load('wood.png')

largefont = pygame.font.SysFont('comicsansms',50)
mediumfont = pygame.font.SysFont('comicsansms',25)
smallfont = pygame.font.SysFont('comicsansms', 35)


white = 255,255,255
black = 0,0,0
red = 198,0,0
bright_red = 255,0,0
green = 0,198,0
bright_green = 0,255,0
blue = 0,0,198
bright_blue = 0,0,255
yellow = 198,198,0
brown = 103,65,44
bright_yellow = 255,255,0
cyanide = 0,255,255
groundheight = 100

        
def text_to_button(text,color,bx,by,bw,bh,size = 'small'):
    textsurf,textrect = text_obj(text,color,size)
    textrect.center = (bx+bw/2,by+bh/2)
    gameDisplay.blit(textsurf,textrect)
    pygame.display.update()
    
def text_obj(text,color,size):
    if size == 'large':
        textsurface = largefont.render(text, True, color)
    if size == 'medium':
        textsurface = mediumfont.render(text, True, color)
    if size == 'small':
        textsurface = smallfont.render(text, True, color)
                          
    return textsurface, textsurface.get_rect()

def buttons(text,x,y,w,h,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if   x<cur[0]< x+ w and  y<cur[1]<y+ h:
        gameDisplay.blit(button_image,(x,y+10))
        text_to_button(text,cyanide,x,y+10,w,h)
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            elif action == 'play':
                house_entrance()
          
    else:
        gameDisplay.blit(button_image,[x,y])
        text_to_button(text,blue,x,y,w,h)

def game_intro():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                gameDisplay.blit(intro_image,[0,0])
                buttons('play', 80,330, 150,65,action ='play')
                buttons('quit', 400,330, 150,65,action ='quit')
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def gameloop():
    score = 0
    playerx = int(screenwidth/5)
    playery = int(screenheight - groundheight)

    newpipe1 = getrandompipe()
    newpipe2 = getrandompipe()

    upperpipes = [
        {'x':screenwidth +200,'y':newpipe1[0]['y']},
        {'x':screenwidth +200+(screenwidth/2),'y':newpipe2[0]['y']},
        ]
    
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    
    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False

    While True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    game_sounds['wing'].play()
        
def getrandompipe():
    pipeheight = game_sprites['pipe'][0].get_height()
    offset = screenheight/3
    y2 = offset + random.randrange(0, int(screenheight - game_sprites['base'].get_height()  - 1.2 *offset))
    pipex = screenwidth + 10
    y1 = pipeheight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe


    
if __name__ == "__main__":
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Super Ball")
    game_sprites['number'] = (pygame.image.load('0.png').convert_alpha(),
                              pygame.image.load('1.png').convert_alpha(),
                              pygame.image.load('2.png').convert_alpha(),
                              pygame.image.load('3.png').convert_alpha(),
                              pygame.image.load('4.png').convert_alpha(),
                              pygame.image.load('5.png').convert_alpha(),
                              pygame.image.load('6.png').convert_alpha(),
                              pygame.image.load('7.png').convert_alpha(),
                              pygame.image.load('8.png').convert_alpha(),
                              pygame.image.load('9.png').convert_alpha(),
                              )
    game_sprites['message'] = pygame.image.load("message1.jpg").convert_alpha()
    game_sprites['base'] = pygame.image.load("road1.jpg").convert_alpha()
    game_sprites['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE),180),
                            pygame.image.load(PIPE).convert_alpha()
                            )
    game_sound['die'] = pygame.mixer.Sound("audio/die.wav")
    game_sound['hit'] = pygame.mixer.Sound("audio/hit.wav")
    game_sound['point'] = pygame.mixer.Sound("audio/point.wav")
    game_sound['swoosh'] = pygame.mixer.Sound("audio/swoosh.wav")
    game_sound['wing'] = pygame.mixer.Sound("audio/wing.wav")

    game_sprites['background'] = pygame.image.load(BACKGROUND).convert()
    game_sprites['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        game_intro()
        game_loop()
    
    
