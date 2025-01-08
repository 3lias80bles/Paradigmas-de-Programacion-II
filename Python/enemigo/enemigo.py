import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 900, 500
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de autos")

# Colores
negro = (0, 0, 0)

# Velocidades
velocidad_jugador = 5

# Cargar imágenes
mototaxy_img = pygame.image.load("Media/motoxd.png")
enemigo1_img = pygame.image.load("Media/carro1.png")
enemigo2_img = pygame.image.load("Media/carro2.png")
enemigo3_img = pygame.image.load("Media/carro3.png")

# Escalar imágenes al tamaño deseado
ancho_auto, alto_auto = 100, 200
mototaxy_img = pygame.transform.scale(mototaxy_img, (ancho_auto, alto_auto))
enemigo1_img = pygame.transform.scale(enemigo1_img, (ancho_auto, alto_auto))
enemigo2_img = pygame.transform.scale(enemigo2_img, (ancho_auto, alto_auto))
enemigo3_img = pygame.transform.scale(enemigo3_img, (ancho_auto, alto_auto))

# Lista de imágenes de enemigos
enemigos_imgs = [enemigo1_img, enemigo2_img, enemigo3_img]

# Configuración de los autos
jugador = pygame.Rect(ancho // 2 - ancho_auto // 2, alto - alto_auto - 50, ancho_auto, alto_auto)  # Inicia en la parte inferior

# Carriles en la carretera
carriles = [alto - alto_auto - 50, alto - alto_auto - 300]  # Dos carriles en la parte inferior

# Crear múltiples enemigos evitando encimarse
def crear_enemigos(cantidad):
    enemigos = []
    ocupado = set()  # Para rastrear carriles ocupados
    for _ in range(cantidad):
        x = random.randint(ancho, ancho + 300)  # Posición inicial fuera de la pantalla
        while True:
            y = random.choice(carriles)  # Elegir un carril aleatoriamente
            if y not in ocupado:  # Asegurar que no se encimen
                ocupado.add(y)
                break
        velocidad = random.randint(-5, -2)  # Velocidad aleatoria hacia la izquierda
        imagen = random.choice(enemigos_imgs)  # Selección aleatoria de imagen
        enemigo = pygame.Rect(x, y, ancho_auto, alto_auto)
        enemigos.append((enemigo, velocidad, imagen))
    return enemigos

enemigos = crear_enemigos(5)  # Crear 5 enemigos

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Función principal
def juego():
    global enemigos

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador (solo en la parte inferior)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and jugador.top > alto // 2:
            jugador.y -= velocidad_jugador
        if teclas[pygame.K_DOWN] and jugador.bottom < alto:
            jugador.y += velocidad_jugador

        # Movimiento de los enemigos
        for i, (enemigo, velocidad, imagen) in enumerate(enemigos):
            enemigo.x += velocidad
            if enemigo.right < 0:  # Si el enemigo sale por la izquierda
                enemigo.x = random.randint(ancho, ancho + 300)  # Reiniciar desde el borde derecho
                ocupado = set(e[0].y for e in enemigos)  # Carriles ocupados por otros enemigos
                while True:
                    enemigo.y = random.choice(carriles)  # Elegir un carril aleatorio
                    if enemigo.y not in ocupado:  # Asegurar que no se encimen
                        break
                enemigos[i] = (enemigo, velocidad, imagen)  # Actualizar en la lista

        # Detectar colisión
        for enemigo, _, _ in enemigos:
            if jugador.colliderect(enemigo):
                #print("¡Colisión detectada!")
                # Reiniciar posiciones
                jugador.y = alto - alto_auto - 50
                enemigos = crear_enemigos(5)

        # Dibujar en la pantalla
        pantalla.fill(negro)
        pantalla.blit(mototaxy_img, (jugador.x, jugador.y))  # Dibujar imagen del jugador
        for enemigo, _, imagen in enemigos:
            pantalla.blit(imagen, (enemigo.x, enemigo.y))  # Dibujar imagen del enemigo
        pygame.display.flip()

        # Controlar FPS
        reloj.tick(60)

if __name__ == "__main__":
    juego()
