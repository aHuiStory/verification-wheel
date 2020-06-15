import pygame
import time


class Question:
    def __init__(self, question, vw_settings, screen, vw_stats):
        """例化 一道题目"""
        self.vw_settings = vw_settings
        self.screen = screen
        self.vw_stats = vw_stats

        self.ask = question["Ask"]
        self.opts = []
        self.answer = question["Answer"]
        self.info = question["Info"]
        self.opt_numbers = len(question) - 3
        self.translate_me(question)

        self.left_pos = self.screen.get_rect().left + 160

    def translate_me(self, question):
        for opt_num in range(self.opt_numbers):
            self.opts.append(question["Opt" + str(opt_num)])
            # print("Opt"+str(opt_num), question["Opt"+str(opt_num)])

    def gen_answer(self):
        if self.answer == "Option0":
            self.vw_stats.cur_answer = pygame.K_a
        elif self.answer == "Option1":
            self.vw_stats.cur_answer = pygame.K_b
        elif self.answer == "Option2":
            self.vw_stats.cur_answer = pygame.K_c
        elif self.answer == "Option3":
            self.vw_stats.cur_answer = pygame.K_d

    def ask_question(self):
        font_ask = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 22)
        font_opt = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 18)

        ask_obj = font_ask.render(self.ask, True, self.vw_settings.text_color, self.vw_settings.bg_color)
        ask_rect_obj = ask_obj.get_rect()
        ask_rect_obj.centery = self.screen.get_rect().centery - 95
        ask_rect_obj.left = self.left_pos
        self.screen.blit(ask_obj, ask_rect_obj)

        for opt_num in range(self.opt_numbers):
            opt_obj = font_opt.render(self.opts[opt_num], True, self.vw_settings.text_color, self.vw_settings.bg_color)
            opt_rect_obj = opt_obj.get_rect()
            opt_rect_obj.centery = self.screen.get_rect().centery - 65 + opt_num * 20
            opt_rect_obj.left = self.left_pos
            self.screen.blit(opt_obj, opt_rect_obj)
        # time.sleep(15)
        # self.vw_stats.game_active = False

    def give_tips(self):
        font_tip = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 15)
        tip_obj = font_tip.render(self.info, True, self.vw_settings.text_color, self.vw_settings.bg_color)
        tip_rect_obj = tip_obj.get_rect()
        tip_rect_obj.centery = self.screen.get_rect().centery + 95
        tip_rect_obj.left = self.left_pos
        self.screen.blit(tip_obj, tip_rect_obj)


