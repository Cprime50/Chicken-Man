import pygame
import os
import math

pygame.init()
x = 800
y = 600
screen = pygame.display.set_mode((x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
