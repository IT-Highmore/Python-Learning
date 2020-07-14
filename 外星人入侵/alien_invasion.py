import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建游戏屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置游戏标题
    pygame.display.set_caption('Alien Invasion')

    # 创建一个用于游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人组
    aliens = Group()

    # 创建外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 开始游戏主循环
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)

run_game()

