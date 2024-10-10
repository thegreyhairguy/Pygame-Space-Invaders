import pygame 
import math
import random

pygame.init()

clock =pygame.time.Clock()
#create the screen 
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((800, 600))
#background
background = pygame.image.load('Background.jpg')
background = pygame.transform.scale(background, (800, 600))
#icon
icon = pygame.image.load('starfighter.png')
pygame.display.set_icon(icon)
#pygame clock

#player=========================================================
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 520
playerX_change = 0

def player(x,y):
  screen.blit(playerImg,(x,y))

#enemies==========================================================

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


def enemy(x,y,i):
  screen.blit(enemyImg[i],(x,y))



#game Loop========================================================
running = True
while running:
  screen.fill((0,0,0))
  screen.blit(background, (0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -3
      if event.key == pygame.K_RIGHT:
        playerX_change = 3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0

  #player movement================================================================
  player(playerX,playerY)
  playerX += playerX_change
  #setting boundry of the screen
  if playerX <= 0:
    playerX = 0
  elif playerX >736:
    playerX = 736
  
  #enemy Movement=================================================================
  #movements for enemy
  for i in range(num_of_enemies): 
    enemyX[i] += enemyX_change[i]
    # Boundry for enemy
    if enemyX[i]<= 0:
      enemyX_change[i] = 2
      enemyY[i] += enemyY_change[i]
    elif enemyX[i] >736:
      enemyX_change[i] = -2
      enemyY[i] += enemyY_change[i]
      
    enemy(enemyX[i],enemyY[i],i)

    
  clock.tick(60)
  pygame.display.update()