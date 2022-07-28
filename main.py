import math
import pygame
import random
import time

# initialization
pygame.init()

# BACKGROUND
screen = pygame.display.set_mode((800, 600))

# TIME
clock = pygame.time.Clock()

# Creation du titre
pygame.display.set_caption("Marie Haut")
iconJeu = pygame.image.load('IMAGES/mario.png')
pygame.display.set_icon(iconJeu)

# GAMEOVER ECRAN
gameoverBackground = pygame.image.load('IMAGES/gameover1.png')


def gameover(x, y):
    screen.blit(gameoverBackground, (x, y))


# SCORE
score_valeur = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10


def aff_score(x, y):
    score = font.render("Nb de vie : " + str(score_valeur), True, (255, 255, 255))
    screen.blit(score, (x, y))


# TIMER

temps_valeur = 30
pygame.time.set_timer(pygame.USEREVENT, 1000)
tempsX = 500
tempsY = 10

# MARIO
# MARIO IMAGE
marioIcon = pygame.image.load('IMAGES/mario.png')
# MARIO IMAGE SIZE
marioIcon = pygame.transform.scale(marioIcon, (60, 60))

# MARIO POSITION
marioIconX = 370
marioIconY = 100

# MARIO VARIABLE POUR DEPLACEMENT
marioIconChangeX = 0
marioIconChangeY = 0


def mario(x, y):
    screen.blit(marioIcon, (x, y))


# PIECE

pieceIcon = pygame.image.load('IMAGES/coeur8bit.png')
pieceIcon = pygame.transform.scale(pieceIcon, (30, 30))
pieceIconX = random.randint(0, 740)
pieceIconY = random.randint(0, 540)


def piece(x, y):
    screen.blit(pieceIcon, (x, y))


# Goomba

goombaIcon = pygame.image.load('IMAGES/goomba.png')
goombaIcon = pygame.transform.scale(goombaIcon, (60, 60))
goombaIconX = random.randint(0, 800)
goombaIconY = random.randint(0, 600)
goombaIconchangeX = 3
goombaIconchangeY = 1


def goomba(x, y):
    screen.blit(goombaIcon, (x, y))


# SYSTEME DE COLLISION
# COLLISION MARIO GOOMBA
def check_collisionmg(mariox, marioy, goombax, goombay):
    distance = math.sqrt((math.pow(mariox - goombax, 2)) + (math.pow(marioy - goombay, 2)))
    if distance < 50:
        return True
    else:
        return False


# COLLISION MARIO PIECE
def check_collisionmp(mariox, marioy, piecex, piecey):
    distancemp = math.sqrt((math.pow(mariox - piecex, 2)) + (math.pow(marioy - piecey, 2)))
    if distancemp < 50:
        return True
    else:
        return False


# BOUCLE DU JEU

running = True
while running:

    # BACKGROUND
    screen.fill((0, 100, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TIMER BOUCLE

        # DEPLACEMENT MARIO DROITE/GAUCHE
        if event.type == pygame.KEYDOWN:
            # DEPLACEMENT GAUCHE
            if event.key == pygame.K_LEFT:
                marioIconChangeX = -2
            # DEPLACEMENT DROITE
            if event.key == pygame.K_RIGHT:
                marioIconChangeX = 2
        # STOP DEPLACEMENT MARIO
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                marioIconChangeX = 0

            # DEPLACEMENT MARIO HAUT/BAS
        if event.type == pygame.KEYDOWN:
            # DEPLACEMENT HAUT
            if event.key == pygame.K_UP:
                marioIconChangeY = -2
            # DEPLACEMENT BAS
            if event.key == pygame.K_DOWN:
                marioIconChangeY = 2

        # STOP DEPLACEMENT MARIO
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                marioIconChangeY = 0

    marioIconX += marioIconChangeX
    # BARRIÈRE GAUCHE DROITE
    if marioIconX <= 0:
        marioIconX = 0
    elif marioIconX >= 740:
        marioIconX = 740

    marioIconY += marioIconChangeY
    # BARRIÈRE GAUCHE DROITE
    if marioIconY <= 0:
        marioIconY = 0
    elif marioIconY >= 540:
        marioIconY = 540

    # DEPLACEMENT GOOMBA
    goombaIconX += goombaIconchangeX
    goombaIconY += goombaIconchangeY
    # BARRIERE DROITE GAUCHE
    if goombaIconX <= 0:
        goombaIconchangeX = random.randint(1, 2)
    elif goombaIconX >= 740:
        goombaIconchangeX = random.randint(-2, -1)

    # BARRIERE HAUT BAS
    if goombaIconY <= 0:
        goombaIconchangeY = random.randint(1, 2)
    elif goombaIconY >= 540:
        goombaIconchangeY = random.randint(-2, -1)

    # COLLISION MARIO PIECE
    collisionMP = check_collisionmp(marioIconX, marioIconY, pieceIconX, pieceIconY)
    if collisionMP:
        pieceIconX = random.randint(0, 800)
        pieceIconY = random.randint(0, 600)

    # SCORE +1
    if collisionMP:
        score_valeur += 1

    # COLLISION MARIO GOOMBA
    collisionMG = check_collisionmg(marioIconX, marioIconY, goombaIconX, goombaIconY)
    if collisionMG:
        # running = False
        screen.fill((100, 0, 0))
        time.sleep(0.5)
        score_valeur -= 1
        time.sleep(0.2)
        goombaIconX = random.randint(0, 800)
        goombaIconY = random.randint(0, 600)
    if score_valeur < 0:
        # running = False

        running = False

    # APPEL DE LA FONCTION
    mario(marioIconX, marioIconY)
    piece(pieceIconX, pieceIconY)
    goomba(goombaIconX, goombaIconY)
    aff_score(scoreX, scoreY)

    # Pour la mise a jour de l'écran
    pygame.display.update()

gameover(0, 0)
pygame.display.update()
time.sleep(5)
pygame.quit()


