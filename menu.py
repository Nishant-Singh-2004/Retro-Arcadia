import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Retro Arcade Menu")

# Load custom fonts
title_font = pygame.font.Font("arcadeClassic.ttf", 50)
subtitle_font = pygame.font.Font("Orbitron.ttf", 20)
button_font = pygame.font.Font("PressStart2P.ttf", 20)
credits_font = pygame.font.Font("ComicSansMS.ttf", 20)

# Function to draw the menu
def draw_menu():
    # Load background image
    background = pygame.image.load('Retro Arcadia.png')
    screen.blit(background, (0, 0))

    # Render game titles and buttons
    title_text = title_font.render("Retro    Arcadia", True, (255, 255, 255))
    screen.blit(title_text, (420, 50))
    
    subtitle_text = subtitle_font.render("Choose the Game Below", True, (255, 255, 255))
    screen.blit(subtitle_text, (420, 110))

    # Developer credits
    dev_text = credits_font.render("Developed by: Shrushranto, Suraj", True, (255, 255, 255))
    screen.blit(dev_text, (450, 500))  
    dev_text1 = credits_font.render("Priyanshu, Nishant", True, (255, 255, 255))
    screen.blit(dev_text1, (590, 530)) 

    # Button texts and positions
    button_texts = ["Flappy Bird", "Car Racing", "Space Invader", "Meteor Blaster", "Ping Pong", "Tetris"]
    global button_positions
    button_positions = [(420, 150), (420, 190), (420, 230), (420, 270), (420, 310), (420, 350)]
    
    for i, text in enumerate(button_texts):
        button_text = button_font.render(text, True, (255, 255, 255))
        screen.blit(button_text, button_positions[i])

    pygame.display.update()

# Game start functions (no changes required here)
def start_flappy_bird():
    subprocess.run(["python", "flappy/flapmain.py"])

def start_car_racing():
    subprocess.run(["python", "CarRacing/project.py"])

def start_space_invader():
    subprocess.run(["python", "SpaceInvader/main.py"])

def start_meteor_blaster():
    subprocess.run(["python", "meteorBlaster/main.py"])

def start_pingpong():
    subprocess.run(["python", "pingpong.py"])

def start_tetris():
    subprocess.run(["python", "Tetris/code/main.py"])

# Main menu function
def main_menu():
    draw_menu()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Button interaction checks
                if button_positions[0][0] <= mouse_pos[0] <= button_positions[0][0] + 200 and button_positions[0][1] <= mouse_pos[1] <= button_positions[0][1] + 40:
                    start_flappy_bird()
                elif button_positions[1][0] <= mouse_pos[0] <= button_positions[1][0] + 200 and button_positions[1][1] <= mouse_pos[1] <= button_positions[1][1] + 40:
                    start_car_racing()
                elif button_positions[2][0] <= mouse_pos[0] <= button_positions[2][0] + 200 and button_positions[2][1] <= mouse_pos[1] <= button_positions[2][1] + 40:
                    start_space_invader()
                elif button_positions[3][0] <= mouse_pos[0] <= button_positions[3][0] + 200 and button_positions[3][1] <= mouse_pos[1] <= button_positions[3][1] + 40:
                    start_meteor_blaster()
                elif button_positions[4][0] <= mouse_pos[0] <= button_positions[4][0] + 200 and button_positions[4][1] <= mouse_pos[1] <= button_positions[4][1] + 40:
                    start_pingpong()
                elif button_positions[5][0] <= mouse_pos[0] <= button_positions[5][0] + 200 and button_positions[5][1] <= mouse_pos[1] <= button_positions[5][1] + 40:
                    start_tetris()

        pygame.display.update()

# Main menu execution
if __name__ == "__main__":
    main_menu()
