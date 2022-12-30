import pygame
import numpy as np


class Particule:
    def __init__(self):
        self.angle = 0
        self.image = pygame.image.load("projectile.png")
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.rotozoom(self.image, -90, 0.5)
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 297
        self.rotation_point = np.array([101 + 50, 144 + 300])
        self.vect_distancetocenter = np.array([self.rect.center[0], self.rect.center[1]]) - self.rotation_point
        self.distance = np.linalg.norm(self.vect_distancetocenter)

    def rotate_canon(self):
        rad_angle = self.angle * np.pi / 180
        normalized = self.vect_distancetocenter/self.distance
        rad_angle += np.arccos(np.dot(normalized, np.array([1, 0])))
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect()
        vect_position = np.array([np.cos(rad_angle), -np.sin(rad_angle)]) * self.distance
        target_center = self.rotation_point + vect_position
        self.rect.center = target_center
