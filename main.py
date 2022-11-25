import pygame
import os
pygame.font.init()

WIDTH , HEIGHT = 900,500

SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55,40

WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Space Invader")

WHITE = (255,255,255)
BLACK = (65,65,65)

BORDER = pygame.Rect(WIDTH/2 - 5, 0 , 5 , HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# yellow_score = 10


MAX_BULLETS = 3


YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT + 2


FPS = 60
VEL = 5
BULLET_VEL = 7

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), -90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets' , 'space.png')),(WIDTH , HEIGHT))


    

def draw_window(red, yellow,red_bullet,yellow_bullet ,yellow_health , red_health):
    # WIN.fill(WHITE)
    WIN.blit(SPACE , (0,0))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1,WHITE)
    WIN.blit(red_health_text , (WIDTH -red_health_text.get_width() -10,10))
    WIN.blit(yellow_health_text , (10,10))

    pygame.draw.rect( WIN , BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP , yellow)
    WIN.blit(RED_SPACESHIP, red)

    for bullet in red_bullet:
        pygame.draw.rect(WIN , 'RED' , bullet)
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN , 'YELLOW' , bullet)


    pygame.display.update()

def yellow_handling_Movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.height < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y +yellow.width < 500:
        yellow.y += VEL

def red_handling_Movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x  > BORDER.x + 5:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + red.height < 900 :
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y +red.width < 500:
        red.y += VEL

def handle_bullet(yellow_bullet, red_bullet , yellow , red):
    for bullet in yellow_bullet:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullet.remove(bullet)

    for bullet in red_bullet:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullet.remove(bullet)
        elif bullet.x < 0 :
            red_bullet.remove(bullet)
                        
def winner(text):
    draw_text = WINNER_FONT.render(text ,1, WHITE)
    WIN.blit(draw_text,(WIDTH/2-draw_text.get_width()/2 ,HEIGHT/2 -draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullet = []
    red_bullet = []

    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                
                if True: 
                	if event.key == pygame.K_LCTRL and len(yellow_bullet) <=MAX_BULLETS:
              	 		bullet = pygame.Rect(yellow.x + yellow.width ,yellow.y +yellow.height/2, 10 ,5)			
              	 		yellow_bullet.append(bullet)


                #if event.key == pygame.K_RCTRL :
                #or len(red_bullet) <=if True:
                if True:
                	if event.key == pygame.K_RCTRL and len(red_bullet) <= MAX_BULLETS:
                    		bullet = pygame.Rect(red.x ,red.y +red.height/2 ,10 , 5)
                    		red_bullet.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0 :
            winner_text = "Yellow Wins"
        if yellow_health <=0 :
            winner_text = "Red_Wins"
        if winner_text != "":
            winner(winner_text)
            break
                
        handle_bullet(yellow_bullet, red_bullet, yellow, red)

        keys_pressed = pygame.key.get_pressed()

        yellow_handling_Movement(keys_pressed , yellow)
        red_handling_Movement(keys_pressed , red)

        draw_window(red, yellow,red_bullet,yellow_bullet ,yellow_health , red_health)
        
        # print(winner_text)

    main()

if __name__ == "__main__" :
    main()
