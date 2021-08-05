import pygame
import random
import time

pygame.init()


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (255,255,0)
blue = (0,50,198)
green = (0, 200, 0)
clock = pygame.time.Clock()
car_width = 70
bright_red = (255,0,0)
grey = (192,192,192)

bright_green = (0,255,0)
font = pygame.font.SysFont('comicsansms',100)
gameDisplay = pygame.display.set_mode((display_width,display_height))
car_img3 = pygame.image.load('car3.jpg')
pygame.display.set_icon(car_img3)
pygame.display.set_caption('careful')
car_img = pygame.image.load('ambulance.png')
car_img1 = pygame.image.load('pinkcar.png')
car_img4 = pygame.image.load('redcar.png')
car_img5 = pygame.image.load('bluecar.png')
car_img6 = pygame.image.load("yellowcar.png")
button_image = pygame.image.load('car button.png')
road = pygame.image.load('road.png')
background = pygame.image.load('car_background.jpg')
crash_sound = pygame.mixer.Sound('carcrash.wav')
star_img = pygame.image.load('star.png')
largefont = pygame.font.SysFont('comicsansms',80)
smallfont = pygame.font.SysFont('comicsansms',35)
mediumfont = pygame.font.SysFont('comicsanssms',50)



def crashsound(crash_sound):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
def paused():
    paused = True
    message_to_screen('paused')
    screen_text = font1.render('press C to continue and Q to quit',False, (255,255,0))
    gameDisplay.blit(screen_text,(100,400))

    pygame.display.update()

    while paused:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    paused = False
                    pygame.mixer.music.unpause()
        

def things_dodged(count):
    font = pygame.font.SysFont('Arial',35)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))
def points(count):
    font = pygame.font.SysFont('Arial',35)
    text = font.render('Stars: ' + str(count), True, red)
    gameDisplay.blit(text, (200,0))
def car(x,y):
    gameDisplay.blit(car_img,(x,y))

def things(thingx,thingy,thingw,thingh):
    gameDisplay.blit(car_img4,[thingx,thingy])
    
def things1(thingx1,thingy1,thingw1,thingh1):
    gameDisplay.blit(car_img5,[thingx1,thingy1])
    
def things2(thingx2,thingy2,thingw2,thingh2):
    gameDisplay.blit(car_img1,[thingx2,thingy2])
    
def things3(thingx3,thingy3,thingw3,thingh3):
    gameDisplay.blit(car_img6,[thingx3,thingy3])
    

def text_to_button(text,color,bx,by,bw,bh,size = 'small'):
    textsurface,textrect = text_obj(text,color,size)
    textrect.center = (bx+bw/2,by+bh/2)
    gameDisplay.blit(textsurface,textrect)
    pygame.display.update()

def text_obj(text,color,size):
    if size == 'small':
        textsurf = smallfont.render(text,True,color)
    if size == 'medium':
        textsurf = mediumfont.render(text,True,color)
    if size == 'large':
        textsurf = largefont.render(text,True,color)
    return textsurf,textsurf.get_rect()


def buttons(text,x,y,w,h,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x<cur[0]<x+w and y<cur[1]<y+h:
        gameDisplay.blit(button_image,(x,y+10))

        if click[0] == 1 and action != None:
            if action == 'play':
                gameloop()
    else:
        gameDisplay.blit(button_image,[x,y])
        #text_to_button(text,grey,x,y,w,h)
def crash():
    pygame.mixer.music.stop()
    textsurf,textrect = text_obj("You Crashed!",blue,size = 'large')
    textrect.center = (display_width/2,display_height/2)
    gameDisplay.blit(textsurf,textrect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            buttons('click', -4,400,200,199,action ='play')
        
        pygame.display.update()
        clock.tick(15)

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
            gameDisplay.blit(background,[0,0])
    
            buttons('click', -4,400,200,199,action ='play')
            
        pygame.display.update()
        clock.tick(15)
        

def gameloop():
    
    pygame.mixer.music.load('carmusic.wav')
    pygame.mixer.music.play(-1)
    road = pygame.image.load('road.png').convert()
    x = int(400)
    y = int(400)
    x_change = int(0)
    y_change = int(0)
    car_speed = int(0)
    y1 = int(0)
    thing_startx1 = int(random.randrange(0,400))
    thing_starty1 = int(-600)
    thing_speed1 = int(10)
    thing_startx2 = int(random.randrange(0,400))
    thing_starty2 = int(-450)
    thing_speed2 = int(10)
    thing_startx3 = int(random.randrange(0,800))
    thing_starty3 = int(-300)
    thing_speed3 = int(10)
    thing_width = int(70)
    thing_height = int(70)
    thing_startx = int(random.randrange(500,800-80))
    thing_starty = int(-300)
    thing_speed = int(10)
    dodged = 0
    car_width = 70
    starx = random.randrange(50,800-100)
    stary = random.randrange(0,600)
    star = 0 
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = int(-15)
                    y_change = int(0)
                if event.key == pygame.K_RIGHT:
                    x_change = int(15)
                    y_change = int(0)
                if event.key == pygame.K_UP:
                    x_change = int(0)
                    y_change = int(-15)
                if event.key == pygame.K_DOWN:
                    x_change = int(0)
                    y_change = int(15)
                if event.key == pygame.K_p:
                    paused()
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

       
        x += x_change
        y += y_change
        y1 += 5
        

        rel_y = int(y1 % road.get_rect().height)
        gameDisplay.blit(road,[0, rel_y - road.get_rect().height])
        if y1 < display_height:
            gameDisplay.blit(road,[0,rel_y])
        if rel_y < display_height:
            gameDisplay.blit(road,(0,rel_y))
            
        things(thing_startx,thing_starty,thing_width,thing_height)
        thing_starty += thing_speed
        things1(thing_startx1,thing_starty1,thing_width,thing_height)
        thing_starty1 += thing_speed1
        things3(thing_startx3,thing_starty3,thing_width,thing_height)
        thing_starty3 += thing_speed1
        gameDisplay.blit(star_img,(starx,stary))
        points(star)
        car(x,y)
        things_dodged(dodged)

        if x < 0:
            x = 0
        if x + car_width > 800:
            x = 800 - car_width
        if y < 0:
            y = 0
        if y + 70 > 600:
            y = 600 - 70

        if thing_starty1 > display_height:
            thing_starty1 = 0 - thing_height
            thing_startx1 = random.randrange(0,400)
            dodged += 1
            y1 += 5
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(500, 800 - 70)
            dodged += 1
            #thing_speed += 1
        if thing_starty2 > display_height:
            thing_starty2 = 0 - thing_height
            thing_startx2 = random.randrange(0, thing_startx - 70)
            dodged += 1
        if thing_starty3 > display_height:
            thing_starty3 = 0 - thing_height
            thing_startx3 = random.randrange(0, thing_startx - 70)
            dodged += 1
        
        if star >= 10:
            things2(thing_startx2,thing_starty2,thing_width,thing_height)
            thing_starty2 += thing_speed2
        if star >= 20:
            things3(thing_startx3,thing_starty3,thing_width,thing_height)
            thing_starty3 += thing_speed3
            
        if x > thing_startx and x < thing_startx + 70 or x + 70 > thing_startx and x + 70 < thing_startx + 70:
            if y > thing_starty and y < thing_starty + 70:
                crashsound(crash_sound)
                crash()
            elif y + 70 > thing_starty and y + 70 < thing_starty + 70:
                crashsound(crash_sound)
                crash()
        
        if x > thing_startx1 and x < thing_startx1 + 70 or x + 70 > thing_startx1 and x + 70 < thing_startx1 + 70:
            if y > thing_starty1 and y < thing_starty1 + 70:
                crashsound(crash_sound)
                crash()
            elif y + 70 > thing_starty1 and y + 70 < thing_starty1 + 70:
                crashsound(crash_sound)
                crash()


        if x > thing_startx2 and x < thing_startx2 + 70 or x + 70 > thing_startx2 and x + 70 < thing_startx2 + 70:
            if y > thing_starty2 and y < thing_starty2 + 70:
                crashsound(crash_sound)
                crash()
            elif y + 70 > thing_starty2 and y + 70 < thing_starty2 + 70:
                crashsound(crash_sound)
                crash()
        if x > thing_startx3 and x < thing_startx3 + 70 or x + 70 > thing_startx3 and x + 70 < thing_startx3 + 70:
            if y > thing_starty3 and y < thing_starty3 + 70:
                crashsound(crash_sound)
                crash()
            elif y + 70 > thing_starty3 and y + 70 < thing_starty3 + 70:
                crashsound(crash_sound)
                crash()

        if x > starx and x < starx + 80 or x + 70 > starx and x + 70 < starx + 80:
            if y > stary and y < stary + 80:
                starx = random.randrange(0,800 -80)
                stary = random.randrange(0,600 -80)
                star += 1
            elif y + 70 > stary and y + 70 < stary + 80:
                starx = random.randrange(0,800 - 80)
                stary = random.randrange(0,600 -80)
                star += 1
                
    
        pygame.display.update()
        clock.tick(35)

game_intro()
gameloop()
pygame.quit()
quit()



                
        


