import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de autos")

# Colores
negro = (0, 0, 0)

# Velocidades
velocidad_jugador = 5
velocidad_enemigo = -3  # Movimiento hacia la izquierda

# Cargar imágenes
##mototaxy_img = pygame.image.load("Media/moto.png")
enemigo_img = pygame.image.load("Media/carro1.png")

# Escalar imágenes al tamaño deseado
ancho_auto, alto_auto = 100, 300
##mototaxy_img = pygame.transform.scale(mototaxy_img, (ancho_auto, alto_auto))
enemigo_img = pygame.transform.scale(enemigo_img, (ancho_auto, alto_auto))

# Configuración de los autos
##jugador = pygame.Rect(ancho // 2 - ancho_auto // 2, alto // 2 - alto_auto // 2, ancho_auto, alto_auto)
enemigo = pygame.Rect(ancho, alto // 2 - alto_auto // 2, ancho_auto, alto_auto)

# Reloj para controlar FPS
reloj = pygame.time.Clock()


# Función principal
def juego():
    global enemigo

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        ##if teclas[pygame.K_UP] and jugador.top > 0:
            ##jugador.y -= velocidad_jugador
        ##if teclas[pygame.K_DOWN] and jugador.bottom < alto:
            ##jugador.y += velocidad_jugador

        # Movimiento del enemigo
        enemigo.x += velocidad_enemigo
        if enemigo.right < 0:  # Si el enemigo sale por la izquierda
            enemigo.x = ancho  # Reiniciar desde el borde derecho

        # Detectar colisión
        ##if jugador.colliderect(enemigo):

            # Reiniciar posiciones
            ##jugador.y = alto // 2 - alto_auto // 2
            enemigo.x = ancho

        # Dibujar en la pantalla
        pantalla.fill(negro)
        ##pantalla.blit(mototaxy_img, (jugador.x, jugador.y))  # Dibujar imagen del jugador
        pantalla.blit(enemigo_img, (enemigo.x, enemigo.y))  # Dibujar imagen del enemigo
        pygame.display.flip()

        # Controlar FPS
        reloj.tick(60)

if __name__ == "__main__":
    juego()
