import pygame
import random
import time
from random import randint
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (190,0,0)
yellow = (200,200,0)
blue = (0,50,198)
green = (0, 190, 0)
bright_green =(0,255,0)
bright_red = (255,0,0)
bright_yellow = (255,255,0)
purple = (148,54,124)

background1 = pygame.image.load('candy_background1.png')
background2 = pygame.image.load('candy_background.jpg')
candy_1 = pygame.image.load('candy1.png')
candy_2 = pygame.image.load('candy2.png')
candy_3 = pygame.image.load('candy3.png')
candy_4 = pygame.image.load('candy4.png')
candy_5 = pygame.image.load('candy5.png')
candy_plate = pygame.image.load('candyplate.png')
font = pygame.font.SysFont('Arial',35)
font1 = pygame.font.SysFont('comicsansms',80)
gameDisplay = pygame.display.set_mode((900,600))
pygame.display.set_caption('candy fair')
fps = 30
clock = pygame.time.Clock()
pygame.display.update()
            
def paused():
    pause = True
    message_to_screen('Paused')
    screen_text = font.render('press C to continue and Q to quit', False, (0,100,255))
    gameDisplay.blit(screen_text,[250,350])
    pygame.display.update()
    while pause:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
def intro():
    intro = True
    gameDisplay.blit(background2,[0,0])
    message_to_screen('Candy Fair!!!')
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        button("play",150,500,100,50,bright_green,green,actions = 'play')
        button("control",400,500,100,50,bright_yellow,yellow,actions = 'control')
        button("quit",650,500,100,50,bright_red,red,actions = 'quit')
        
        pygame.display.update()
        clock.tick(5)
            
def text_obj(text,font):
    textsurface = font1.render(text, True, red)
    return textsurface,textsurface.get_rect()
def text_obj2(text,font):
    textsurface2 = font.render(text,True,purple)
    return textsurface2,textsurface2.get_rect()
def button_text(text,buttonx,buttony,buttonw,buttonh):
    textsurf,textrect = text_obj2(text,font)
    textrect.center = ((buttonx+buttonw/2),(buttony+buttonh/2))
    gameDisplay.blit(textsurf,textrect)
def button(text,x,y,w,h,ac,ic,actions = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if   x<mouse[0]<x+w and   y<mouse[1]<y+h:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and actions != None:
            if actions == 'quit':
                pygame.quit()
                quit()
            if actions == 'control':
                pass
            if actions == 'play':
                gameloop()
            
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    button_text(text,x,y,w,h)
def message_to_screen(text):
    largeText = font1
    text_surf,text_rect = text_obj(text,font1)
    text_rect.center = (900/2, 600/2)
    gameDisplay.blit(text_surf,text_rect)
    
def gameloop():
    pygame.mixer.music.load("candymusic.wav")
    pygame.mixer.music.play(-1)
    candies = [candy_2,candy_4,candy_5]
    display_color = candies[random.randint(0,2)]
    
    paddle_x = 300
    paddle_y = 450
    paddle_x_change = 0
    paddle_y_change = 0
    paddle_height = 50
    paddle_width = 100
    
    candy_velocity = 35
    candy_radius = 30
    candy_x = random.randrange(0, 900 - 30)
    candy_y = - 800


    candy_x1 = random.randrange(0, 900- 30)
    candy_y1 = -900

    candy_x2 = random.randrange(0, 900 - 30)
    candy_y2 = - 700

    candy_x3 = random.randrange(0, 900 - 30)
    candy_y3 = - 600

    candy_x4 = random.randrange(0, 900 - 30)
    candy_y4 = -500

    paddle_velocity = 45
    delay = 50
    score = 0
    total = 0
    timer = 100
    dt = 1
    gameExit = False
    while not gameExit:
        pygame.time.delay(delay)
        gameDisplay.blit(background1,[0,0])
        screen_text = font.render('Score: {0}/{1}'.format(score,total),False,(0,0,0))
        gameDisplay.blit(screen_text,(10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_x_change = -paddle_velocity
                    paddle_y_change = 0
                if event.key == pygame.K_RIGHT:
                    paddle_x_change = paddle_velocity
                    paddle_y_change = 0
                if event.key == pygame.K_UP:
                    paddle_y_change = -paddle_velocity
                    paddle_x_change = 0
                if event.key == pygame.K_DOWN:
                    paddle_y_change = paddle_velocity
                    paddle_x_change = 0
                if event.key == pygame.K_p:
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_y_change = 0
        timer -= dt
        candy_y += candy_velocity
        candy_y1 += candy_velocity
        candy_y3 += candy_velocity
    
        paddle_x += paddle_x_change
        paddle_y += paddle_y_change
        
        if timer <= 0:
            timer = 100
            display_color = candies[random.randint(0,2)]
            
        if paddle_x >= 900:
            paddle_x = 10
        if paddle_x <= 0:
            paddle_x = 900 - 100
        if paddle_y <= 0:
            paddle_y = 0
        if paddle_y >= 430:
            paddle_y = 450

        if candy_y > 530 - 50 :
            candy_x = random.randrange(0, 900 - 30)
            candy_y = - 900
        if candy_y1 > 530 - 50:
            candy_x1 = random.randrange(0, 900 - 30)
            candy_y1 = -20
            total += 1
        if candy_y2 > 530 - 50:
            candy_x2 = random.randrange(0, 900 - 30)
            candy_y2 = -10

        if candy_y3 > 530 - 50:
            candy_x3 = random.randrange(0, 900 - 30)
            candy_y3 = -20
        if candy_y4 > 530 - 50:
            candy_x4 = random.randrange(0, 900 - 30)
            candy_y4 = -10
        if display_color == candy_4:
            if candy_x > paddle_x and candy_x < paddle_x + paddle_width or candy_x + 30 > paddle_x and candy_x + 30 < paddle_x + paddle_width:
                if candy_y > paddle_y and candy_y < paddle_y + paddle_height:
                    candy_x = random.randrange(0, 900 - 30)
                    candy_y = - 900
                    score += 1
                    pygame.display.update()
                    
                elif candy_y + 30 > paddle_y and candy_y + 30 < paddle_y + paddle_width:
                    candy_x = random.randrange(0, 900 - 30)
                    candy_y = - 900
                    score += 1
                    pygame.display.update()
        if display_color == candy_5:
            if candy_x1 > paddle_x and candy_x1 < paddle_x + paddle_width or candy_x1 + 30 > paddle_x and candy_x1 + 30 < paddle_x + paddle_width:
                if candy_y1 > paddle_y and candy_y1 < paddle_y + paddle_height:
                    candy_x1 = random.randrange(0, 900 - 30)
                    candy_y1 = -20
                    score += 1
                    pygame.display.update()
                elif candy_y1 + 30 > paddle_y and candy_y1 + 30 < paddle_y + paddle_width:
                    candy_x1 = random.randrange(0, 900 - 30)
                    candy_y1 = -20
                    score += 1
                    pygame.display.update()
        if display_color == candy_2:
            if candy_x3 > paddle_x and candy_x3 < paddle_x + paddle_width or candy_x3 + 30 > paddle_x and candy_x3 + 30 < paddle_x + paddle_width:
                if candy_y3 > paddle_y and candy_y3 < paddle_y + paddle_height:
                    candy_x3 = random.randrange(0, 900 - 30)
                    candy_y3 = -20
                    score += 1
                    pygame.display.update()
                elif candy_y3 + 30 > paddle_y and candy_y3 + 30 < paddle_y + paddle_width:
                    candy_x3 = random.randrange(0, 900 - 30)
                    candy_y3 = -20
                    score += 1
                    pygame.display.update()
            

                        
        
        gameDisplay.blit(candy_4,[candy_x,candy_y])
        gameDisplay.blit(candy_5,[candy_x1,candy_y1])
        gameDisplay.blit(candy_2,[candy_x3,candy_y3])
        gameDisplay.blit(candy_plate,[paddle_x,paddle_y])
        gameDisplay.blit(display_color,(210,20))
        
        pygame.display.update()
        clock.tick(fps)
intro()             
gameloop()
pygame.quit()
quit()


















            
    
    
