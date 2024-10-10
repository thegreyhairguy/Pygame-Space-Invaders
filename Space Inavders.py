import pygame
import random
import math

clock = pygame.time.Clock()

#initialize pygame module
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))
# set caption
pygame.display.set_caption("Space Invaders")

#Set Icon
icon = pygame.image.load("starfighter.png")
pygame.display.set_icon(icon)


#background
background = pygame.image.load("Background.jpg")

#player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 400
playerX_change = 0

def player(x,y):
  screen.blit(playerImg,(x,y))

#enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
  enemyImg.append(pygame.image.load("alien.png"))
  enemyX.append(random.randint(0,735))
  enemyY.append(random.randint(50,150))
  enemyX_change.append(4)
  enemyY_change.append(40)

# enemyImg = pygame.image.load("alien.png")
# enemyX = random.randint(0,735)
# enemyY = random.randint(50,150)
# enemyX_change = 0.3
# enemyY_change = 60



def enemy(x,y,i):
  screen.blit(enemyImg[i],(x,y))


#bullet
#ready state you can state the bullet on screen
#fire - the bulletr is currently moving

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

def fire_bullet(x,y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(bulletImg,(x+16,y+10))

#gameover
def game_over_text():
  over_font = pygame.font.Font("freesansbold.ttf",64)
  game_over_text = over_font.render("GAME OVER",True,(255,255,255))
  screen.blit(game_over_text,(200,250))


#Collision
score=0
def inCollision(enemyX,enemyY,bulletX,bulletY):
  distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow((enemyY-bulletY),2)))
  if distance <27:
    return True
  else:
    return False
                       
                       

  
#game loop Event
running =True
while running:
  screen.fill((255,255,0))  # screen color with RGB values
  screen.blit(background,(0,0))#background
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -3
      if event.key == pygame.K_RIGHT:
        playerX_change = 3
      if event.key == pygame.K_SPACE:
        if bullet_state is "ready":
          bulletX =playerX
          fire_bullet(bulletX,bulletY)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        playerX_change = 0
      if event.key == pygame.K_RIGHT:
        playerX_change = 0
      if event.key == pygame.K_SPACE:
        fire_bullet(playerX,playerY)

    
  #movements for player 
  playerX += playerX_change
  #setting boundry of the screen
  if playerX <= 0:
    playerX = 0
  elif playerX >736:
    playerX = 736
  
  #mvements for enemy
  for i in range(num_of_enemies):
    #gameover
    if enemyY[i] >300:
      for j in range(num_of_enemies):
        enemyY[j] = 2000
      game_over_text()
      break


        
    enemyX[i] += enemyX_change[i]
    # Boundry for enemy
    if enemyX[i]<= 0:
      enemyX_change[i] = 2
      enemyY[i] += enemyY_change[i]
    elif enemyX[i] >736:
      enemyX_change[i] = -2
      enemyY[i] += enemyY_change[i]
      
    #collision
    collision = inCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    if collision:
      bulletY = 400
      bullet_state = "ready"
      score += 1
      print(score)
      enemyX[i] = random.randint(0,735)
      enemyY[i] = random.randint(50,150)
      
    enemy(enemyX[i],enemyY[i],i)

  
  
  player(playerX,playerY)
  pygame.display.update()

    
  #bullet movement 
  if bullet_state is "fire":
    fire_bullet(bulletX,bulletY)
    bulletY -= bulletY_change

  if bulletY <= 0:
    bulletY = 400
    bullet_state ="ready"

  
  #collision
  collision = inCollision(enemyX,enemyY,bulletX,bulletY)
  if collision:
    bulletY = 400
    bullet_state = "ready"
    score += 1
    print(score)
    enemyX = random.randint(0,735)
    enemyY = random.randint(50,150)
    
  clock.tick(60)
  pygame.display.update()  # update game screen 