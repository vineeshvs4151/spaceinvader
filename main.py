import pygame
import random
import math
from pygame import mixer
# intialize the pygame
pygame.init()
# create the screen or set up screen
screen = pygame.display.set_mode((800, 600))
# setup caption or title for our game
pygame.display.set_caption("Space Invaders")
# setup logo or icon for our game
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerimg = pygame.image.load("space.png")
playerx = 370
playery = 480
playernx = 0
playerny = 0
enemy1 = pygame.image.load("skull.png")
enemy1x = random.randint(0,800)
enemy1y = random.randint(0,100)
enemy1nx=2
bullet=pygame.image.load("bullet.png")
bulletx=0
bullety=0
bulletnx=0
bulletny=9
bullet_state="ready"
bg=pygame.image.load("background.png")
# mixer.music.load("background.wav")
# mixer.music.play(-1)
def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy(x,y):
    screen.blit(enemy1,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
def fire_collision(enemy1x,enemy1y,bulletx,bullety):
    distance=math.sqrt((math.pow(enemy1x-bulletx,2))+(math.pow(enemy1y-bullety,2)))
    if distance<27:
        return True
exist = True
while exist:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exist=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playernx=-7
            if event.key==pygame.K_RIGHT:
                playernx=7
            if event.key==pygame.K_UP:
                playerny=-7
            if event.key==pygame.K_DOWN:
                playerny=7
            if event.key==pygame.K_SPACE:
               if bullet_state=="ready":
                # bs=mixer.Sound('laser.wav')
                # bs.play()
                bulletx=playerx
                bullety=playery
                fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playernx=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerny=0
    playerx+=playernx
    playery+=playerny
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736
    if playery<=300:
        playery=300
    elif playery>=536:
        playery=536
    enemy1x+=enemy1nx
    if enemy1x<=0:
        enemy1nx=2
        enemy1y+=20
    elif enemy1x>=736:
        enemy1nx=-2
        enemy1y+=20
    if enemy1y>=300:
        enemy1y=random.randint(0,100)
    if bullet_state=="fire" :
       bullety-=bulletny
       fire_bullet(bulletx,bullety)
    if bullety<=0:
        bullet_state="ready"
    collision=fire_collision(enemy1x,enemy1y,bulletx,bullety)
    if collision:
        enemy1x=random.randint(0,800)
        enemy1y=random.randint(0,200)
    player(playerx,playery)
    enemy(enemy1x,enemy1y)
    pygame.display.update()
