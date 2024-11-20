import pygame
from display import *   # นำเข้าฟังก์ชันจาก display.py
import question_c as qc

def play_game_select_choice(screen, font):
    score = 0
    running = True

    while running:
        #question, answer, options = generate_choice_question(score)
        generate_question = qc.generate_question(score)
        answer, question = generate_question.create()
        options = generate_question.option()
        button_rects = display_question(question, options, screen, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()

        start_ticks = pygame.time.get_ticks()  # เริ่มจับเวลา
        user_choice = None

        while user_choice is None:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 500  # เวลาเป็นวินาที
            time_left = 7 - elapsed_time

            if time_left <= 0:
                display_score(score, screen)
                return

            # จัดการเหตุการณ์ภายในลูปเพื่อให้เกมสามารถออกได้อย่างราบรื่น
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

            # อัปเดตแถบเวลาที่เหลือ
            display_time_bar(time_left, screen)
            pygame.display.update()  # อัปเดตหน้าจอ

            # รับการเลือกของผู้ใช้
            user_choice = get_user_choice(button_rects)

        if options[user_choice] == answer:
            score += 1
        else:
            display_score(score, screen)
            #display_high_score(score,screen, font)
            return
        
