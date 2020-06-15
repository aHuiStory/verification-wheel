import pygame


class Stats():
    def __init__(self):
        self.game_active = True
        self.answer_en = False
        self.cur_answer = pygame.K_f
        self.info_print_en = False
