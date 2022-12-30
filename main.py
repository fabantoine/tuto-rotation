import pygame
from canon import Canon, Cible
from particule import Particule

pygame.init()
clock = pygame.time.Clock()
CIEL = 0, 200, 255

canon = Canon()
cible = Cible()
cible.reposition(canon.rect)

cible.find_point(96, 139)

particule = Particule()

def main():
    fenetre = pygame.display.set_mode((1260, 480))
    # loop
    loop = True
    # Création d'une image de la taille de la fenêtre
    background = pygame.Surface(fenetre.get_size())

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_UP]:
            canon.angle += 2
            particule.angle += 2
        if user_input[pygame.K_DOWN]:
            canon.angle -= 2
            particule.angle -= 2
        canon.rotation()
        canon.stupid_rotation()
        #canon.angle += 1
        # Superposition du fond ciel
        background.fill(CIEL)
        fenetre.blit(background, (0, 0))
        #fenetre.blit(canon.rotate_surf, (canon.rect.x-39, canon.rect.y))
        fenetre.blit(canon.rotate_surf, (canon.rect.x - 39, canon.rect.y))
        #fenetre.blit(canon.imaged, (canon.rectd.x, canon.rectd.y))
        #fenetre.blit(cible.image, (cible.rect.x, cible.rect.y))
        particule.rotate_canon()
        #fenetre.blit(particule.image, (particule.rect.x, particule.rect.y))

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # By calling Clock.tick(10) once per frame, the program will never run
        # at more than 10 frames per second
        clock.tick(60)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
