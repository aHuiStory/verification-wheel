import sys
import pygame
import json
import time
from question import Question


def check_events(vw_settings, vw_stats, screen, question):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif vw_stats.answer_en and event.key == vw_stats.cur_answer:
                print("Well done!")
                vw_stats.game_active = False
            elif vw_stats.answer_en and event.key != vw_stats.cur_answer:
                print("Failed...")
                vw_stats.info_print_en = True
                update_screen(vw_settings, vw_stats, screen, question)
                time.sleep(5)
                vw_stats.game_active = False


def update_screen(vw_settings, vw_stats, screen, question):
    screen.fill(vw_settings.bg_color)
    if not vw_stats.info_print_en:
        question.ask_question()
    else:
        question.give_tips()
    pygame.display.flip()


def get_question(file_path, vw_settings, screen, vw_stats):
    try:
        f_obj = open(file_path, encoding='utf-8')
    except FileNotFoundError:
        print("test file not found, please check.")
        vw_stats.game_active = False
    else:
        question = json.load(f_obj)
        cur_question = Question(question, vw_settings, screen, vw_stats)
        # vw_stats.game_active = False
        vw_stats.answer_en = True
        return cur_question




