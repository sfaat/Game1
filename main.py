import pygame
import random
import math
from pygame import mixer

pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 550))

# change icone and titale
pygame.display.set_caption("space icon")
icon = pygame.image.load('spc.png')
pygame.display.set_icon(icon)

# backgraund
backgraund = pygame.image.load('fulspace.png.')


#backgraundSound

mixer.music.load('background.wav')
mixer.music.play(-1)
# players
playImage = pygame.image.load('rec.png')
playX = 225
playY = 450
# plears_chengX = 0.3
plears_chengX = 0
plears_chengY = 0

# Enemy
EnemyImage = []
EnemyX = []
EnemyY = []
Enemy_chengX = []
Enemy_chengY = []
number_of_Enemy = 6

for i in range(number_of_Enemy):
    EnemyImage.append(pygame.image.load('space.png'))
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(50, 150))
    Enemy_chengX.append(0.1)
    Enemy_chengY.append(40)

# bullet
bulletImage = pygame.image.load('bullet.png')
bulletX = 0

bulletY = 480
bullet_chengX = 0
bullet_chengY = 1
bullet_state = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over

game_over_font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score1=font.render("score :" + str(score),True,(255, 255, 255))
    screen.blit(score1, (x, y))




def game_overText():
    over_text = game_over_font.render("GAME OVER :", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))




def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


def player(x, y):
    screen.blit(playImage, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImage[i], (x, y))


# collision
def isCollision(EnemyX, EnemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(EnemyX - bulletX, 2)) + (math.pow(EnemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    screen.fill((000, 000, 000))
    # backgraund
    screen.blit(backgraund, (0, 0))
    # playY -= 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                plears_chengX = -0.3
            if event.key == pygame.K_RIGHT:
                plears_chengX = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()

                    bulletX = playX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plears_chengX = 0
    # plere
    playX += plears_chengX
    if playX <= 0:
        playX = 0
    elif playX >= 736:
        playX = 736
    # Enamy
    for i in range(number_of_Enemy):
        # game over

        if EnemyY[i] >440:
            for j in range(number_of_Enemy):
                EnemyY[j] = 2000
            game_overText()
            break
        EnemyX[i] += Enemy_chengX[i]
        if EnemyX[i] <= 0:
            Enemy_chengX[i] = 0.1
            EnemyY[i] += Enemy_chengY[i]
        elif EnemyX[i] >= 736:
            Enemy_chengX[i] = -0.1
            EnemyY[i] += Enemy_chengY[i]
        # collison
        collision = isCollision(EnemyX[i], EnemyY[i], bulletX, bulletY)
        if collision:
            Explosion_sound = mixer.Sound('explosion.wav')
            Explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(50, 150)
        enemy(EnemyX[i], EnemyY[i], i)




    # Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_chengY


    player(playX, playY)

    show_score(textX, textY)
    pygame.display.update()
