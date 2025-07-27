import math
import random
import pygame


screenWidth=800
screenHeight=500
playerStartX=370
playerStartY=380
enemyStartYMin=50
enemyStartYMax=150
enemySpeedX=4
enemySpeedY=40
bulletSpeedY=10
collisionDistance=27


pygame.init()


screen=pygame.display.set_mode((screenWidth,screenHeight))


background=pygame.image.load('background.png')


pygame.display.set_caption("Space Invader")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)


playerImg=pygame.image.load('player.png')
playerX=playerStartX
playerY=playerStartY
playerX_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
numOfEnemies=6