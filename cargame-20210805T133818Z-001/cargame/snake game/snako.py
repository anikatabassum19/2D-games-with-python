import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,255,0)
green = (0,255,0)
blue = (0,255,255)
dark_red = (95, 0,0)
dark_blue = (0,0, 70)
bright_red = (255,0,0)
dark_green = (0, 200, 0)
appleThickness = 30
gameDisplay = pygame.display.set_mode((700,700))
pygame.display.set_caption('snako')
img = pygame.image.load('snake1.png')
largefont = pygame.font.SysFont('comicsansms',50)
mediumfont = pygame.font.SysFont('comicsansms',25)
smallfont = pygame.font.SysFont('comicsansms', 35)
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
back_ground1 = pygame.image.load('background2.png')
back_ground2 = pygame.image.load('background3.jpg')
back_ground = pygame.image.load('background.jpg')
apple = pygame.image.load('apple1.png')
tail = pygame.image.load('tail2.png')
tail2 = pygame.image.load('tail.png')
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('Arial', 35)
crash_sound = pygame.mixer.Sound('buzzer.wav')
block_size = 20
direction = 'right'

def crash(crash_sound):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    

def paused():
    paused = True
    message_to_screen("paused",
                          red,
                          -100,
                          'large')
    message_to_screen("press C to continue and Q to quit",
                          blue,
                          -50,
                          'medium')
    pygame.display.update()
    

    while paused:
        
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(black)
        #gameDisplay.blit(back_ground2,[0,0])


def game_intro():
    

    intro = True

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
       # gameDisplay.fill(dark_red)
        gameDisplay.blit(back_ground1,[0,0])
        message_to_screen('Welcome to Snaaakoooo.....',
                          green,
                          -100,
                          size = 'large')
        message_to_screen("Feed your snake with red delicious Apples....!!!",
                          red,
                          -25,
                          size = 'medium' )
        message_to_screen('But if you run over yourself, then, YOU DIE!! :P',
                          red,
                          25,
                          'medium')
        message_to_screen('Press C to continue and Q to quit',
                          blue,
                           100,
                          'small')
        pygame.display.update()
        
        clock.tick(5)
            


    

def text_obj(text,color,size):
    if size == 'large':
        textsurface = largefont.render(text, True, color)
    if size == 'medium':
        textsurface = mediumfont.render(text, True, color)
    if size == 'small':
        textsurface = smallfont.render(text, True, color)
                          
    return textsurface, textsurface.get_rect()


def message_to_screen(msg,color, y_displace = 0, size= 'large'):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, (100,100))
    textsurf,textrect = text_obj(msg,color,size)
    textrect.center = (350,350 + y_displace)
    gameDisplay.blit(textsurf,textrect)


def snake(block_size,snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
        #lej1 = pygame.transform.rotate(tail2, 360)
        lej = pygame.transform.rotate(tail, 180)

    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
        #lej1 = pygame.transform.rotate(tail2, 180)
        lej = tail
    if direction == 'up':

        head = img
        #lej1 = pygame.transform.rotate(tail2,270)
        lej = pygame.transform.rotate(tail,270)
        
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
        #lej1 = pygame.transform.rotate(tail2, 90)
        lej = pygame.transform.rotate(tail,90)
    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        gameDisplay.blit(lej,[XnY[0],XnY[1]])
        #gameDisplay.blit(lej1,(snakelist[0][0],snakelist[0][1]))
        
                #pygame.draw.rect(gameDisplay, dark_green, [XnY[0],XnY[1],block_size,block_size])


def randApplegen():
    randApplex = round(random.randrange(0,700-block_size)) #/10)*10
    randAppley = round(random.randrange(0,700-block_size)) #/10)*10
    return randApplex, randAppley

def gameloop():
    global direction
    global size
    pygame.mixer.music.load('bak_music.wav')
    pygame.mixer.music.play(-1)
        
    direction = 'right'
    lead_x = 200
    lead_y = 200
    lead_x_change = 10
    lead_y_change = 0
    randApplex = round(random.randrange(0,700-block_size)) #/10)*10
    randAppley = round(random.randrange(0,700-block_size)) #/10)*10c
    score = 0
    
    gameExit = False
    gameOver = False
    snakelist = []
    snakelength = 1
    while not gameExit:
        
        while gameOver == True:
            pygame.time.delay(2000)
            pygame.mixer.music.pause()
            gameDisplay.blit(back_ground,[0,0])
            message_to_screen('GameOver',bright_red, y_displace = -50, size = 'large')
            message_to_screen('Wanna play AGGGGAINNN....???',blue, y_displace = 10, size = 'medium')
            message_to_screen('Press C to continue and Q to quit',green,y_displace=50,size = 'medium')
            screen_text = font1.render('score: {0}'.format(score),False, (255,255,255))
            gameDisplay.blit(screen_text,(250,230))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameloop()
                        
                        #gameOver = False
                        pygame.mixer.music.unpause()
                        
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = 20
                    lead_y_change = 0
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -20
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -20
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = 20
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    paused()
        lead_x += lead_x_change
        lead_y += lead_y_change
               
        if lead_x > 700 or lead_x < 0 or lead_y > 700 or lead_y < 0:
            gameOver = True
            crash(crash_sound)
            
        clock.tick(15)

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True
                crash(crash_sound)

        gameDisplay.blit(back_ground2,[0,0])
        gameDisplay.blit(apple,(randApplex,randAppley))
        
        
        #gameDisplay.fill(red, rect = [randApplex,randAppley, appleThickness, appleThickness])
        #gameDisplay.blit(apple,[randApplex[0],randAppley[1]])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        
        

        if len(snakelist) > snakelength:
            del snakelist[0]
        snake(block_size,snakelist)
        screen_text = font1.render('score: {0}'.format(score),False, (255,255,255))
        gameDisplay.blit(screen_text,(10,10))
        pygame.display.update()
        
        
        

     #   if lead_x >= randApplex and lead_x <= randApplex + appleThickness:
      #      if lead_y >= randAppley and lead_y <= randAppley + appleThickness:
       #         randApplex = round(random.randrange(0,700-block_size)) #/10)*10
        #        randAppley = round(random.randrange(0,700-block_size)) #/10)*10
         #       snakelength += 1

        if lead_x > randApplex and lead_x < randApplex + appleThickness or lead_x + block_size > randApplex and lead_x + block_size < randApplex + appleThickness:
             
            if lead_y > randAppley and lead_y < randAppley + appleThickness:
                #randApplex = round(random.randrange(0,700-block_size)) #/10)*10
                #randAppley = round(random.randrange(0,700-block_size)) #/10)*10
                randApplex,randAppley = randApplegen()
                snakelength += 1
                score += 1
                pygame.display.update()
        
            elif lead_y +block_size > randAppley and lead_y + block_size < randAppley + appleThickness:
                #randApplex = round(random.randrange(0,700-block_size)) #/10)*10
                #randAppley = round(random.randrange(0,700-block_size)) #/10)*10
                randApplex,randAppley = randApplegen()
                snakelength += 1
                score += 1
                
                pygame.display.update()

    clock.tick(50)
    pygame.quit()
    quit()

game_intro()
gameloop()












            
