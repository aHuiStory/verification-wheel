import pygame
import vw_function as vf
from setting import Setting
from question import Question
from stats import Stats

file_path = './shelf/test.json'
default_question = {
    "Ask": "What's your name?",
    "Opt0": "Gauss",
    "Opt1": "Wrong",
    "Opt2": "Right",
    "Answer": "Right",
    "Info": "default into"
}


def vw_main():
    pygame.init()
    vw_settings = Setting()
    vw_stats = Stats()
    screen = pygame.display.set_mode(
        (vw_settings.screen_width, vw_settings.screen_height))
    pygame.display.set_caption("Verification wheel")
    # 方案1：从数据库中抽取10道题目，存入一个字典列表中
    cur_question = Question(default_question, vw_settings, screen, vw_stats)
    # 方案2：控制循环次数，每次都从题库中抽取1个题目（不能重复）
    while vw_stats.game_active:

        if not vw_stats.answer_en:
            print("Welcome to Verification Wheel Game!")
            cur_question = vf.get_question(file_path, vw_settings, screen, vw_stats)
            # 将问题打印到屏幕上
            # print(cur_question.ask)
            # 将选项在屏幕上显示
            # print(cur_question.opts)
            # 传递答案
            cur_question.gen_answer()
            vf.update_screen(vw_settings, vw_stats, screen, cur_question)

        vf.check_events(vw_settings, vw_stats, screen, cur_question)


vw_main()




