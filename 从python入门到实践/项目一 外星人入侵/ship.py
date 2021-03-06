import pygame
from  pygame.sprite import Sprite

class Ship(Sprite):

  def __init__(self, ai_settings, screen):
    super(Ship, self).__init__()
    """初始化飞船并设置其初始位置"""
    self.screen = screen
    self.ai_settings = ai_settings

    # 加载飞船图像
    self.image = pygame.image.load('images/ship.bmp')
    # 飞船外接矩阵
    self.rect = self.image.get_rect()
    # 屏幕矩形
    self.screen_rect = screen.get_rect()

    # 将每艘飞船放在屏幕底部中央
    self.center = float(self.rect.centerx)
    # self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # 移动标志
    self.moving_right = False
    self.moving_left = False

  def update(self):
    """根据移动标志调整飞船位置"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed_factor

    if self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed_factor

    # 根据self.center更新react对象
    self.rect.centerx = self.center

  def blitme(self):
    """指定位置绘制飞船"""
    self.screen.blit(self.image, self.rect)


  def center_ship(self):
    """让飞船在屏幕居中"""
    self.center = self.screen_rect.centerx