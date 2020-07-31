import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def __init__(self):



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    # 设置游戏屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置游戏标题
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
