import pygame
import sys

class cargame():
    def __init__(self,max_vel, rotation_vel):
        self.max_vel= max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0

    def game_loop(self):
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()
    

    def car(self):
        pass

