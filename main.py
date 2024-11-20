import pygame
import sys
from display import *   # นำเข้าฟังก์ชันจาก display.py
from game import *      # นำเข้าฟังก์ชันจาก game.py
import button
import song_c

# เริ่มต้นใช้งาน Pygame
pygame.init()

# ตั้งค่าหน้าจอ
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Math Games')

# ตั้งค่าฟอนต์
font = pygame.font.Font(r'font\Matrixtype.ttf', 48)

# สร้างปุ่ม
start_button = button.Button(400,100,'white',(194,194,194))

# โหลดรูปภาพพื้นหลัง
background1_image = pygame.image.load(r"image\main.png")
background1_image = pygame.transform.scale(background1_image, (600, 800))

p_song = song_c.play_music()

# Start playing the first song
#song.play_song(song.current_song_index)
song_c.play_song(p_song.current_song_index, p_song.songs)

p_song.start()

def menu():
    """ฟังก์ชันสำหรับแสดงเมนูเริ่มต้น"""
    running = True
    volume = p_song.volume
    
    while running:
        # แสดงรูปภาพพื้นหลัง
        screen.blit(background1_image, (0, 0))
        #game1_button.draw(screen)
        start_button.draw(screen, 100, 350, 'Start')
        #screen.blit(background_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(mouse_pos):
                    return "Page_1"
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: # Press 'up arrow' to increase volume
                    volume = min(1.0, volume + 0.1)
                    pygame.mixer.music.set_volume(volume)

                elif event.key == pygame.K_DOWN: # Press 'down arrow' to decrease volume
                    volume = max(0.0, volume - 0.1)
                    pygame.mixer.music.set_volume(volume) 
                
                elif event.key == pygame.K_RIGHT: # Prees '->' to next song
                    p_song.next_song()

                elif event.key == pygame.K_LEFT: # Press '<-' to previous song
                    p_song.previous_song()
        
        pygame.display.flip()


# ตรวจสอบว่าโค้ดเริ่มต้นทำงานที่นี่
if __name__ == "__main__":
    while True:
        # แสดงเมนูและรอการเลือก
        current_page = menu()
        
        # ถ้าเลือก Page_1 เริ่มเกมใหม่
        if current_page == "Page_1":
            play_game_select_choice(screen, font)  # เริ่มเกมและรับคะแนน
            # หากคุณต้องการแสดงคะแนนที่ได้ก่อนจะกลับไปที่เมนู สามารถเรียกใช้ฟังก์ชันแสดงคะแนนได้ที่นี่

pygame.quit()  # คำสั่งนี้จะทำงานเมื่อโปรแกรมจะออกจากลูป
sys.exit()     # ออกจากโปรแกรม