import pygame
import button
import sys
import element

question_background = pygame.image.load(r"image\QA.png")
question_background = pygame.transform.scale(question_background, (600, 800))
score_background = pygame.image.load(r"image\SC.png")
score_background = pygame.transform.scale(score_background, (600, 800))

def display_question(question, options, screen, font):
    screen.blit(question_background, (0, 0))
    question_surface = font.render(question, True, (255, 255, 255))
    question_rect = question_surface.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(question_surface, question_rect.topleft)

    button_rects = []
    button_width = 500
    button_height = 100
    spacing = 30

    for i, option in enumerate(options):
        option_surface = font.render(f"{option}", True, (0, 0, 0))
        button_rect = pygame.Rect(50, 200 + (button_height + spacing) * i, button_width, button_height)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)

        text_rect = option_surface.get_rect(center=button_rect.center)
        screen.blit(option_surface, text_rect.topleft)

        button_rects.append(button_rect)

    pygame.display.flip()
    
    return button_rects

def display_time_bar(time_left, screen):
    bar_width = 500  # Width of the time bar
    bar_height = 30  # Height of the time bar
    x = 50  # X position of the bar
    y = 150  # Y position of the bar

    # Calculate the width of the remaining time bar
    remaining_width = (time_left / 7) * bar_width

    # Draw the background of the time bar
    pygame.draw.rect(screen, (200, 200, 200), (x, y, bar_width, bar_height))

    # Draw the remaining time as a colored bar
    pygame.draw.rect(screen, (0, 255, 0), (x, y, remaining_width, bar_height))  # Green color for the time left

    pygame.display.flip()

def get_user_choice(button_rects):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for index, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    return index
    return None

def display_score(score, screen):
    # แสดงรูปภาพพื้นหลัง
    screen.blit(score_background, (0, 0))

    # แสดง score
    #score_surface = font.render(f"Scores : {score}", True, (255, 255, 255))
    score_surface = element.style_2.set(f'Scores : {score}')
    screen.blit(score_surface, (135, 300))



    # ปุ่ม Try Again
    #try_again_button = button.Draw(100, 400, 400, 100, 'white', font, "Try Again")
    #try_again_button.draw(screen)

    try_again_button = button.Button(400,100,'white')
    try_again_button.draw(screen, 100, 400, 'Try Again')

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # ออกจากโปรแกรมเมื่อผู้ใช้กดปิดหน้าต่าง
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if try_again_button.rect.collidepoint(mouse_pos):
                    waiting = False  # ออกจากลูปนี้เพื่อเริ่มเกมใหม่
                    return True  # ส่งค่ากลับเพื่อบอกว่าควรเริ่มเกมใหม่