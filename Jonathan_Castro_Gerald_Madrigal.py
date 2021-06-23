import pygame, sys

import pygame, sys
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1200, 700),0,32)
 
font = pygame.font.SysFont(None, 40)


import random
import os

carpeta_juego =os.path.dirname(__file__)

carpeta_Imagen= os.path.join(carpeta_juego,"Imagen")


#sonidos
pygame.mixer.init()

# explosion=pygame.mixer.Sound("Imagen/explosion.wav")

# ambiente= pygame.mixer.Sound("Imagen/music.ogg")

# ambiente.play()
 
#tamaño del la pantalla
ANCHO = 1200
ALTO = 700

#Fps
FPS = 30

#colores
NEGRO = (0,0,0)
BLANCO =(255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE = (60,63,65)
AZUL = (0,0,255)
H_50DEFE = (94,210,254)
#############################




##############################
class Nave(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()

        self.image = pygame.image.load("Imagen/nave.png").convert()
        self.image.set_colorkey(NEGRO)
        
        self.rect = self.image.get_rect()
        self.radius= 20

        self.rect.center = (400,600)
        #vida de la nave
        self.hp1 = 100
        self.hp2 = 100
        self.hp3 = 100



        #Velocidad inicial
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):

        #Velocidad inicial
        self.velocidad_x = 0
        self.velocidad_y = 0

        #teclas pulsadas
        teclas = pygame.key.get_pressed()

        #mover izquierda
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10
        #mover derecha
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10
        #mover arriba
        if teclas[pygame.K_UP]:
            self.velocidad_y = -10
        #mover abajo
        if teclas[pygame.K_DOWN]:
            self.velocidad_y = 10
        
        #Actualizar velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #limita margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        #limita margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        #limita margen arriba
        if self.rect.top < 0:
            self.rect.top = 0
        #limita margen abajo
        if self.rect.bottom >ALTO:
            self.rect.bottom = ALTO


#nivel 1
class Meteoro(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()

        self.image = pygame.image.load("Imagen/meteoro3.png").convert()
        self.image.set_colorkey(NEGRO)
        
        self.rect = self.image.get_rect()
        self.radius= 100

        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(250)
    
        self.velocidad_x = 8
        self.velocidad_y = 8

    def update(self):
        #Actualizar velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #limita margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x +=random.randrange(7, 10)
        #limita margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -=random.randrange(7, 10)
        #limita margen arriba
        if self.rect.top < 0:
            self.velocidad_y +=random.randrange(7, 10)
        #limita margen abajo
        if self.rect.bottom >ALTO:
            self.velocidad_y  -=random.randrange(7, 10)


#nivel 2
class Meteoro1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Imagen/meteoro2.png").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x= random.randrange(ANCHO)
		self.rect.y = random.randrange(1,10)
		self.speedy = 15

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > ALTO + 10 or self.rect.left < 10 or self.rect.right > ANCHO + 10:
			self.rect.x = random.randrange(ANCHO)
			self.rect.y = random.randrange(1,10)
			self.speedy = 15


#nivel 3
class Meteoro2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("Imagen/meteoro2.png").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
        ###################################
		self.rect.y= random.randrange(ALTO)
		self.rect.x = random.randrange(1,10)
		self.speedx = 15

	def update(self):
		self.rect.x += self.speedx
		if self.rect.top > ANCHO + 10 or self.rect.right < 10 or self.rect.right > ANCHO + 10:
			self.rect.y = random.randrange(ALTO)
			self.rect.x = random.randrange(1,10)
			self.speedx = 15


#creacion de ventana,titulo
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))

#barra de vida de la nave
def mostrar_vida(pantalla, x, y, porcentaje):
	largo = 200
	ancho = 20
	rectangulo = (porcentaje / 100) * largo
	borde = pygame.Rect(x, y, largo, ancho)
	rectangulo = pygame.Rect(x, y, rectangulo, ancho)
	pygame.draw.rect(pantalla, AZUL, rectangulo)
	pygame.draw.rect(pantalla, ROJO, borde, 2)

def cronometro(pantalla , x , y):
    aux = 1
    while True:
        pantalla.blit(fondo, [0,0])
        Tiempo = pygame.time.get_ticks()/1000
        if aux == Tiempo:
            aux += 1
            print(Tiempo)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        contador = font.render("Tiempo : "+str(Tiempo),0,(120,70,0))
        pantalla.blit(contador,(100,100))
        pygame.display.update()


#Escritor de texto
def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#Fondo de pantalla
pygame.display.set_caption("Nuevo juego")
Clock = pygame.time.Clock()
fondo = pygame.image.load("Imagen/fondo.jpg").convert()
game_f = pygame.image.load("Imagen/game_overr.jpg").convert()
#Grupos de sprites e instalaciones
sprites = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
meteorito = pygame.sprite.Group()
meteorito_A = pygame.sprite.Group()

################
nave = Nave()
sprites.add(nave)


#blucle del juego

 
def main_menu():
    click = False
    while True:

        pantalla.blit(fondo, [0, 0])

        draw_text('SKY IS THE LIMIT', font, BLANCO, screen, 530, 20)
        draw_text('Nivel 1', font, BLANCO, screen, 60, 60)
        draw_text('Nivel 2', font, BLANCO, screen, 60, 160)
        draw_text('Nivel 3', font, BLANCO, screen, 60, 260)
        draw_text('Creditos', font, BLANCO, screen, 60, 600)
        draw_text('Puntajes', font, BLANCO, screen, 1000, 600)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        button_4 = pygame.Rect(50, 640, 200, 50)
        button_5 = pygame.Rect(950, 640, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game1()
                
        if button_2.collidepoint((mx, my)):
            if click:
                game2()
        if button_3.collidepoint((mx, my)):
            if click:
                game3()
        if button_4.collidepoint((mx, my)):
            if click:
                game4()
        if button_5.collidepoint((mx, my)):
            if click:
                game5()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        pygame.draw.rect(screen, (255, 0, 0), button_5)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def game1():
    ejecutando = True
    while ejecutando:
        Clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

    #Infinita creacion de los meteoritos
        if not meteoros:
            for x in range(7):
                meteoro = Meteoro()
                meteoros.add(meteoro)


        #Actualizacion de sprites
        sprites.update()
        meteoros.update()
        

    #colisiones de la nave y meteoritos
        colision_nave = pygame.sprite.spritecollide(nave,meteoros,True)
        if colision_nave:
            #explosion.play()
            nave.hp1 -=34

        if nave.hp1 <= 0:
            game_over()
        
        
            
    ###############
        pantalla.blit(fondo, [0, 0])
        sprites.draw(pantalla)
        meteoros.draw(pantalla)
        
        
    #texto en la pantalla
        mostrar_vida(pantalla, 595, 10, nave.hp1)

    #######################
        
        pygame.display.flip()


def game2():
    ejecutando = True
    while ejecutando:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

    #Infinita creacion de los meteoritos
        if not meteoros:
            for x in range(7):
                meteoro = Meteoro()
                meteoros.add(meteoro)


        if not meteorito:
            for x in range(2):
                meteoros1 = Meteoro1()
                meteorito.add(meteoros1)


 
        #Actualizacion de sprites
        sprites.update()
        meteoros.update()
        meteorito.update()
        


    #colisiones de la nave y meteoritos
        colision_nave = pygame.sprite.spritecollide(nave,meteoros,True)
        if colision_nave:
            #explosion.play()
            nave.hp2 -=34
        
        colision_nave = pygame.sprite.spritecollide(nave,meteorito,True)
        if colision_nave:
            #explosion.play()
            nave.hp2 -=34

        if nave.hp2 <= 0:
            game_over()
            
        
    ###############
        pantalla.blit(fondo, [0, 0])
        sprites.draw(pantalla)
        meteoros.draw(pantalla)
        meteorito.draw(pantalla)
        
        
    #texto en la pantalla
        mostrar_vida(pantalla, 595, 10, nave.hp2)

    #######################
        pygame.display.flip()

def game3():
    ejecutando = True
    while ejecutando:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

    #Infinita creacion de los meteoritos
        if not meteoros:
            for x in range(5):
                meteoro = Meteoro()
                meteoros.add(meteoro)


        if not meteorito:
            for x in range(1):
                meteoros1 = Meteoro1()
                meteorito.add(meteoros1)

        if not meteorito_A:
            for x in range(1):
                meteoros2 = Meteoro2()
                meteorito_A.add(meteoros2)


 
        #Actualizacion de sprites
        sprites.update()
        meteoros.update()
        meteorito.update()
        meteorito_A.update()


    #colisiones de la nave y meteoritos
        colision_nave = pygame.sprite.spritecollide(nave,meteoros,True)
        if colision_nave:
            #explosion.play()
            nave.hp3 -=34
        
        colision_nave = pygame.sprite.spritecollide(nave,meteorito,True)
        if colision_nave:
            #explosion.play()
            nave.hp3 -=34

        colision_nave = pygame.sprite.spritecollide(nave,meteorito_A,True)
        if colision_nave:
            #explosion.play()
            nave.hp3 -=34
        if nave.hp3 <= 0:
            game_over()
            
            
        
    ###############
        pantalla.blit(fondo, [0, 0])
        sprites.draw(pantalla)
        meteoros.draw(pantalla)
        meteorito.draw(pantalla)
        meteorito_A.draw(pantalla)
        
    #texto en la pantalla
        mostrar_vida(pantalla, 595, 10, nave.hp3)

    #######################
        pygame.display.flip()





def game_over():
    click = False

    while True:
 
        pantalla.blit(game_f, [0, 0])

        draw_text('Regresar', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
                break
                
       
        pygame.draw.rect(screen, (255, 0, 0), button_1)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 

        
        
def game4():
    running = True
    while running:
        pantalla.blit(fondo, [0, 0])
 
        draw_text('País de producción Costa Rica', font, BLANCO, screen, 480, 0)
        draw_text('Tecnológico de Costa Rica', font, BLANCO, screen, 500, 50)
        draw_text('Carrera Ingeniería en Computadores', font, BLANCO, screen, 430, 100)
        draw_text('Taller de Programación', font, BLANCO, screen, 520, 150)
        draw_text('Año 2021', font, BLANCO, screen, 600, 200)
        draw_text('Grupo 3', font, BLANCO, screen, 600, 250)
        draw_text('Profesor Leonardo Araya Martinez', font, BLANCO, screen, 430, 300)
        draw_text('Python 3.9.5', font, BLANCO, screen, 590, 350)
        draw_text('Autores', font, BLANCO, screen, 610, 400)
        draw_text('Jonathan Castro Mendoza', font, BLANCO, screen, 490, 450)
        draw_text('Gerald Madrigal Rodríguez ', font, BLANCO, screen, 490, 500)
        draw_text('Autores de módulos', font, BLANCO, screen, 550, 550)
        draw_text('progrmación facil', font, BLANCO, screen, 565, 600)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def game5():
    running = True
    while running:
        screen.blit(fondo, [0,0]) 
        draw_text('MEJORES PUNTAJES', font, BLANCO, screen, 450, 200)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)


main_menu()