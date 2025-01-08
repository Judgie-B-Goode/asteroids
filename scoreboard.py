import pygame

class Scoreboard():
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 32, bold=True)
        self.score_label = self.font.render("SCORE:", True, pygame.Color("white"))