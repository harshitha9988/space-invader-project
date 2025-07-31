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


for _i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,screenWidth-64))

    enemyY.append(random.randint(enemyStartYMin,enemyStartYMax))
    enemyX_change.append(enemySpeedX)
    enemyY_change.append(enemySpeedY)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=playerStartY
bulletXchange=0
bulletYchange=bulletSpeedY
bullet_state="ready"


scoreValue=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


overFont=pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):

    score=font.render("Score: "+str(scoreValue),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():

    over_text=overFont.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):

    screen.blit(playerImg,(x,y))

def enemy(x,y,i):

    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):

    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance<collisionDistance



running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bullet=playerX
                fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change=0


    playerX+=playerX_change
    playerX=max(0,min(playerX,screenWidth-64))


    for i in range(numOfEnemies):
        if enemyY[i]>340:
            for j in range(numOfEnemies):
                enemyY[j]=2000
            game_over_text()
            break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0 or enemyX[i]>=screenWidth-64:
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change[i]

        if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY=playerStartY
            bullet_state="ready"
            scoreValue+=1
            enemyX[i]=random.randint(0,screenWidth-64)
            enemyY[i]=random.randint(enemyStartYMin,enemyStartYMax)

        enemy(enemyX[i],enemyY[i],i)

    if bulletY<=0:
        bulletY=playerStartY
        bullet_state="ready"
    elif bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletYchange

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()