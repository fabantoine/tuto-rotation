import pygame


class Canon:
    def __init__(self):
        self.angle = 0
        self.rotate_surf = pygame.Surface((280, 288))
        self.image = pygame.image.load("canon.png")
        self.rotate_surf.blit(self.image, (39, 0))
        #self.rotate_surf.set_colorkey((0, 0, 0))
        self.origin_rot = self.rotate_surf
        self.origin_rect = self.origin_rot.get_rect()
        self.rect = self.rotate_surf.get_rect()
        self.rect.x = 50
        self.rect.y = 300
        self.origin_rect.x = self.rect.x
        self.origin_rect.y = self.rect.y
        self.imaged = pygame.image.load("canon.png")
        self.rectd = self.imaged.get_rect()
        self.rectd.x = 200
        self.rectd.y = 200
        self.ctest = self.rectd.center

    def rotation(self):
        self.rotate_surf = pygame.transform.rotate(self.origin_rot, self.angle)
        self.rect = self.rotate_surf.get_rect()
        self.rect.center = self.origin_rect.center

    def stupid_rotation(self):
        self.imaged = pygame.transform.rotozoom(self.image, self.angle, 1)
        self.rectd = self.imaged.get_rect()
        self.rectd.center = self.ctest


class Cible:
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.draw = pygame.draw.circle(self.image, (255, 255, 255),(5, 5), 5)
        self.rect = self.image.get_rect()

    def reposition(self, rect):
        self.rect.x = rect.x
        self.rect.y = rect.y

    def find_point(self, x, y):
        self.rect.x += x
        self.rect.y += y