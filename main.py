import math
import os
import random

import pygame
from pygame.locals import *

pygame.init()

#Create screen
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()                #To set our fps but I don't need this because it makes our animation scuffy but we can add this later

#Background
bGround_Top = pygame.image.load(os.path.join('background.png'))
bGround_B = pygame.image.load(os.path.join('Background_buttom.jpg'))
#bGround_Sky = pygame.image.load(os.path.join('sky.jpg'))
game_overImg = pygame.image.load(os.path.join('Sprites/Gameover.jpg'))

#Character Animations
    #Player animations
            #Player Default animation
playerImg =[None]*5
for pieindex in range(1,5):
    playerImg[pieindex - 1] = pygame.image.load(os.path.join("Hero", "Chicken Up", "Up" + str(pieindex)+ ".png")).convert_alpha()
    pieindex +=1

            #Player move left while walking Animation
left = [None] *5
for pieindex in range (1, 5):
    left[pieindex - 1] = pygame.image.load(os.path.join("Hero", "Chicken Left", "Left" + str(pieindex) + ".png")).convert_alpha()
    pieindex +=1
    #You can also  do this by creating a list and it should still work
    #[pygame.image.load(os.path.join("Hero","Chicken Left", "Left1.png")),
       # pygame.image.load(os.path.join("Hero", "Chicken Left", "Left2.png")),
       #pygame.image.load(os.path.join("Hero", "Chicken Left", "Left3.png")),
       #pygame.image.load(os.path.join("Hero", "Chicken Left", "Left4.png"))]

                #Player move right while walking Animation
right = [None] *5
for pieindex in range (1, 5):
    right[pieindex - 1] = pygame.image.load(os.path.join("Hero", "Chicken Right", "Right" + str(pieindex) + ".png")).convert_alpha()
    pieindex +=1

    #Enemy Animation
                #Enemy Bird animation
enemyImg = [None] *5
for pieindex in range (1, 5):
        enemyImg[pieindex - 1] = pygame.image.load(os.path.join("Enemy", "Bird", "B" + str(pieindex) + ".png")).convert_alpha()
        pieindex +=1
                #Enemy Kooba Animation
                        #Enemy Redkooba
RedkoobaImg = [None] *13
for pieindex in range (1, 13):
    RedkoobaImg[pieindex - 1] = pygame.image.load(os.path.join("Sprites", "Red kooba" , "RedKooba"  + str(pieindex) + ".png"))
    pieindex +=1
                        #Enemy Redkooba Low Hp
RedkoobaLowImg = [None] *13
for pieindex in range (1, 13):
    RedkoobaLowImg[pieindex - 1] = pygame.image.load(os.path.join("Sprites", "Red kooba low" , "RedKoobal"  + str(pieindex) + ".png"))
    pieindex +=1
                        #Boss Animation
boss_Img = [None] *13
for pieindex_1 in range (1, 13):
    boss_Img[pieindex_1 - 1] = pygame.image.load(os.path.join("Sprites", "boss" , "boss"  + str(pieindex) + ".png"))
    pieindex_1 +=1
    if pieindex_1 == [10]:
        boss_bullet_state = "fire"
    else:
        boss_bullet_state = "ready"


#Game Title and Game Icon
pygame.display.set_caption("Chicken Man")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Planyer and Player Movement
#playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 500      
playerX_change = 0          #How much player will move on our xaxis
playerY_change = 0          #How much player will move on our yaxis
move_left = False           #This will trigger our player animation moving leftwards, we say false so it doesnt activate until a condition is met
move_right = False          #Player animation moving rightwards, We give this a false default value because we dont actually want our player to move until a button is pressed
Fly = False                    #player fly
Fly_Low = False                 #Player fly down to walk
stepindex = 0
game_over = False


#Enemy
enemy_right = True
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4
enemy_pos = []


for i in range(num_of_enemies):
    enemyImage.append(enemyImg)
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(-10,30 ))      #We use this for timing our enemy will spawn, we calculate the speed at which they are moving downwards in  the y axis and then place them at a location up up above above window axis, the enemy will spawn when they have reached our window
    enemyX_change.append(0)
    enemyY_change.append(0.8)

#Enemy RedKooba0
redKmove = True          #to proc red kooba animation
redKoobaX = random.randint(0, 735)
redKoobaY = random.randint(-10, -9)
redKY_change = 0.4
redKX_change = 0
redkoobImg = RedkoobaImg
num_of_redkoobas = 4
stepinde = 0                #Step index but for kooba
RedkoobaLow = False
redkoobLowImg = RedkoobaLowImg

#Enemy RedKooba1
redKmove1 = True          #to proc red kooba animation
redKoobaX1 = random.randint(0, 735)
redKoobaY1 = random.randint(-10, -9)
redKY_change1 = 0.4
redKX_change1 = 0
redkoobImg = RedkoobaImg                #Step index but for kooba
RedkoobaLow1 = False

#Boss
boss_move = False          #to proc red kooba animation
bossX = 300
bossY = -10
bossY_change = 0.2
bossX_change = 0
bossimg = boss_Img
stepind = 0                #Step index but for kooba
hit_countB = 0


#Bullet
bulletImg = pygame.image.load("bulletegg.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"

#Boss bullet
boss_bullet_image = pygame.image.load("bulletegg.png")
boss_bullet_img = []
boss_bulletX_change = []
boss_bulletY_change = []
num_of_boss_bullets = 3
boss_bulletY = []
boss_bullet_state = "ready"

#Use pythagorean theorem to make bullet postion display like a triangle shape
boss_bullet_pos = [(bossX, bossY - boss_bulletY_change),
                   (bossX, - ( boss_bulletY_change * math.sqrt(3) / 2), bossY + (boss_bulletY_change / 2)),
                   (bossX, + ( boss_bulletY_change * math.sqrt(3) / 2), bossY + (boss_bulletY_change / 2))]

for position in range(boss_bullet_pos):
    boss_bullet_img.append(boss_bullet_image)
    boss_bulletY.append(boss_bullet_pos)
    
#Health
#Player Health
#playerhealth_img = pygame.image.load("life.png")                   # Add later

#Redkooba
RedKooba_Health = 100
hit_count = 0
RedKooba_Health1 = 100
hit_count1 = 0

#gameOver
Game_over = False

#score
score_value = 0

# Font
font = pygame.font.Font('freesansbold.ttf',32) 


#functions
def player(x,y):        #Animation
    global stepindex
   
    if stepindex >= 4:                  #Our number here is (4) bc the amount of images we are displaying for animation is 3 and we want to return value back to (0)after all 3 images have been loaded
        stepindex = 0
    
    if move_left:
        screen.blit(left[stepindex], (x, y))
        stepindex +=1
    elif move_right:
        screen.blit(right[stepindex], (x, y))
        stepindex +=1    
    elif Fly:
        screen.blit(playerImg[stepindex], (x, y))
        stepindex +=1
    elif Fly_Low:
        screen.blit(playerImg[stepindex], (x, y))
        stepindex +=1
def show_score(x, y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))  #this code renders the text of variable score_value on the screen, since the text is an integer we need to fist convert it to a string using the str type. this is known as type casting, also we can show what colour we want the text to appear as using the RGB value
    screen.blit(score, (x,y))
 
def enemy(x , y, i):
    global stepindex
    
    if stepindex >= 4:
        stepindex = 0

    if enemy_right:
        screen.blit(enemyImage[i][stepindex], (x, y))
        stepindex +=1

def kooba(x , y):
    global stepinde
    
    if stepinde >= 12:
        stepinde = 0

    if redKmove:
        screen.blit(redkoobImg[stepinde], (x, y))
        stepinde +=1
    
    elif RedkoobaLow:
        screen.blit(redkoobLowImg[stepinde], (x, y))
        stepinde +=1
def kooba1(x, y ):
    global stepinde
    if redKmove1:
        screen.blit(redkoobImg[stepinde], (x, y))
        stepinde +=1
    
    elif RedkoobaLow1:
        screen.blit(redkoobLowImg[stepinde], (x, y))
        stepinde +=1

def boss(x,y):
    global stepind
    if stepind >= 12:
        stepind = 0
    if boss_move:
        screen.blit(boss_Img[stepind], (x, y))
        stepind +=1
    
#def player_Health():
    #screen.blit(playerhealth_img, ((x,y)))             #Add later

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y + 10))

def boss_fire_bullet(x, y):
    global boss_bullet_state
    boss_bullet_state = "fire"
    screen.blit(boss_bullet_img, (x + 20, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX- bulletX,2)) + (math.pow(enemyY - bulletY,2))) #Math equation to calc distance between two ponts and the midpoint D=Sqrt(x2 - x1)^2 + (y2 - y1)^2..... In python squarerrot is assigned using math.Sqrt and raise to power (^) is assigned using maath.pow(equation, number we want to raise too)
    if distance < 40:
        return True
    else:
        return False
    
def isCollisionRed(redKoobaX, redKoobaY, bulletX, bulletY):
    distanceRed = math.sqrt((math.pow(redKoobaX- bulletX,2)) + (math.pow(redKoobaY - bulletY,2))) #Math equation to calc distance between two ponts and the midpoint D=Sqrt(x2 - x1)^2 + (y2 - y1)^2..... In python squarerrot is assigned using math.Sqrt and raise to power (^) is assigned using maath.pow(equation, number we want to raise too)
    if distanceRed < 40:
        return True
    else:
        return False
def isCollisionRed1(redKoobaX1, redKoobaY1, bulletX, bulletY):
    distanceRed = math.sqrt((math.pow(redKoobaX1- bulletX,2)) + (math.pow(redKoobaY1 - bulletY,2))) #Math equation to calc distance between two ponts and the midpoint D=Sqrt(x2 - x1)^2 + (y2 - y1)^2..... In python squarerrot is assigned using math.Sqrt and raise to power (^) is assigned using maath.pow(equation, number we want to raise too)
    if distanceRed < 40:
        return True
    else:
        return False
def isCollisionBoss(bossX, bossY, bulletX, bulletY):
    distanceB = math.sqrt((math.pow(bossX- bulletX,2)) + (math.pow(bossY - bulletY,2))) #Math equation to calc distance between two ponts and the midpoint D=Sqrt(x2 - x1)^2 + (y2 - y1)^2..... In python squarerrot is assigned using math.Sqrt and raise to power (^) is assigned using maath.pow(equation, number we want to raise too)
    if distanceB < 70:             #Distance to detect Collision
        return True
    else:
        return False
    
#def enemyColide(redKoobaX, redKoobaY):
    

#our loop
running = True
while running:

   
    #screen display
    screen.fill((0,0,0))
    screen.blit(bGround_Top, (0, 165))     #Background_Top
    screen.blit(bGround_B, (0, 563))
    #screen.blit(game_overImg, (0,0))        # Background Bottom
    
     
    #close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    #Keyboard Movement
    userInput = pygame.key.get_pressed()
   
    if Fly == True and userInput [pygame.K_LEFT]:
           playerX_change = -30
           move_left = False
           move_right = False
           Fly = True 
    elif userInput [pygame.K_LEFT]:
        playerX_change = -20
        move_left = True
        move_right = False     #True means our characrter will moved left once the key is pressed
     
    elif Fly == True and userInput [pygame.K_RIGHT]:
           playerX_change = +30
           move_left = False
           move_right = False
           Fly = True 
     
    elif  userInput [pygame.K_RIGHT]:
        playerX_change = +20
        move_left = False
        move_right = True
        
         
    
    elif userInput [pygame.K_UP]:
       playerY_change = -15

       move_left = False
       move_right = False
       Fly = True
       
           
       #playerX_change = 0
      # stepindex += 1      #playerImg Image movement
       #pygame.time.delay(10)  #playerImg animation delay
    
    elif userInput [pygame.K_DOWN]:
        playerY_change = +20
        
    else:
       move_left = False
       move_right = False
       Fly = False
       Fly_Low = True
       playerX_change = 0
       playerY_change = 0
    
    if userInput [pygame.K_SPACE]:
        Fly = True
        if bullet_state == "ready":
            bulletX = playerX
            bulletY = playerY
            fire_bullet(bulletX, bulletY)

    if Fly:
        move_left = False
        move_right = False
    
    #enemy_right = True
    '''for i in range (num_of_enemies):
        enemyY[i] += enemyY_change[i]
    enemy(enemyX[i], enemyY[i], i)'''

   # enemyY += enemyY_Change

    pygame.time.delay(30)

    if playerY <538:
        Fly = True
        pygame.time.delay(40)

    #Player Boundary
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    
    if playerY <=400:
        playerY = 400
        #playerY_change = +1
        Fly = False
        Fly_Low = True

#Where player can walk and where player can fly
    if playerY >= 500:
         playerY = 500
         Fly = False
         Fly_Low = True
    if playerY < 500:
        Fly_Low = False
        Fly = True

    #Enemy Boundry, Enemy movement and Game over 
    #Movement
    for i in range(num_of_enemies):  #Our collision and game over needs to be under this for loop here for it to apply to all our enemies #For some reason the other three enemys only display when we use this so all of our other functions such as our collision, we need to put it under this for loop so it can apply to all enemys otherwise it will apply to just one of them
        #Prevnt koobabros from colliding together and overlapping
        #for j in range (i, num_of_enemies):
           
        #Go off screen once boss arrives
        if boss_move == True:
            enemyY[i] = -100
        #Colision 
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
          print('nice shot')
          bulletY = 480
          bullet_state = "ready"
          enemyX[i] = random.randint(0, 735)
          enemyY[i] = random.randint(-150, -80)
        enemy(enemyX[i], enemyY[i], i)
        #enemyX[j] += enemyX_change[j]
        enemyY[i] += enemyY_change[i]

        #Game over and Boundary
        if enemyY[i] >= playerY - 20:
           Game_over = True

#Kooba boundary, movement and game over
    #Movement
        
        #redKmove = True
    redKoobaY += redKY_change
    kooba(redKoobaX, redKoobaY)   
    #collision
    collisionRed = isCollisionRed(redKoobaX, redKoobaY, bulletX, bulletY)
    if collisionRed:
          hit_count += 1            #Count each time the enemy gets hit
          if hit_count == 1:
              health = -50
              bulletY = 480
              bullet_state = "ready"
              RedkoobaLow = True
              redKmove = False
             
          elif hit_count == 2:
                health = -50
                bulletY = 480
                bullet_state = "ready"
                redKoobaX = random.randint(0, 735)
                redKoobaY = random.randint(-150, -80)
                RedkoobaLow = False
                redKmove = True
          if hit_count >2:
                hit_count=0

    #Game over
    if redKoobaY >= playerY - 20:
        Game_over = True        #terrible use of variable name but each game ov er names are different 
            
         
    kooba(redKoobaX, redKoobaY)
    #Kooba boundary, movement and game over
    #Movement
        
        #redKmove = True
    redKoobaY1 += redKY_change1
    kooba1(redKoobaX1, redKoobaY1)

    #Redkooba bullet
    if redKoobaY1 >=1:
        bullet_state1 = "fire"
        if bullet_state1 == "ready":
            bulletX1 = redKoobaX1
            bulletY1 = redKoobaY1
            fire_bullet1(bulletX1, bulletY1)
    
    bossY += bossY_change
    boss(bossX, bossY) 

    #collision
    collisionRed1 = isCollisionRed1(redKoobaX1, redKoobaY1, bulletX, bulletY)
    if collisionRed1:
          hit_count1 += 1            #Count each time the enemy gets hit
          if hit_count1 == 1:
              health1 = -50
              bulletY = 480
              bullet_state = "ready"
              RedkoobaLow1 = True
              redKmove1 = False
              
          elif hit_count1 == 2:
                health1 = -50
                bulletY = 480
                bullet_state = "ready"
                redKoobaX1 = random.randint(0, 735)
                redKoobaY1 = random.randint(-150, -80)
                RedkoobaLow1 = False
                redKmove1 = True
          if hit_count1 >2:
                hit_count1=0

    if redKoobaY >= playerY - 20:
             Game_over = True

    #Preveent Collision between redkooba bros
    distanceClash = math.sqrt((math.pow(redKoobaX- redKoobaX1,2)) + (math.pow(redKoobaY - redKoobaY1,2)))
    if distanceClash < 40:
        redKoobaX += random.randint(0, 735)
    elif distanceClash > 40:
        pass

    #Every Enemy displays out of screen if boss shows up
    if boss_move == True:
        enemyY[i] = -20
        redKoobaY = -64
        redKoobaY1 = -64

    #boss animation wont proc unless he in our window   
    if bossY <-10:
        boss_move = False
    elif bossY >= 1:
        boss_move = True

    #Shooting Boss
    collisionBoss = isCollisionBoss(bossX, bossY, bulletX, bulletY)
    if collisionBoss:
        hit_countB += 1            #Count each time the enemy gets hit
        if hit_countB < 10:
            bulletY = 480
            bullet_state = "ready"
        elif hit_countB ==10:
                bulletY = 480
                bossY = -100
                bullet_state = "ready"
        if hit_countB >10:
                hit_countB=0
    if bossY >= playerY - 20:
        Game_over = True
    

   #Bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #boss Bullet state and Movement
    if boss_bullet_state == "ready":
        boss_bullet_pos = (bossX , bossY)
        boss_fire_bullet(boss_bullet_pos)
    
    #GameOver
    if Game_over:
        screen.blit(game_overImg, (0,0))
        game_over = True
        redKoobaY = 1000
        move_left = False
        move_right = False
        move_left = False
        move_right = False
        Fly = False
        Fly_Low = False
        enemy_right = False
        redKmove = False 
        enemyY[i] = 1000
        bossY = 1000
        playerY = 1000
        

    #screen.blit(playerhealth_img, (700,500))               display this later
    playerX += playerX_change
    playerY += playerY_change 
    pygame.time.delay(20)
               #time delay in our loop
    player(playerX,playerY)
    pygame.display.update()
    clock.tick(20)            #To set our Fps