好的，以下是一个简单的超级玛丽游戏的Python代码示例：

```python
import pygame

# 初始化游戏
pygame.init()

# 设置游戏窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario")

# 加载玛丽的图像
mario_image = pygame.image.load("mario.png")
mario_rect = mario_image.get_rect()
mario_rect.centerx = screen_width // 2
mario_rect.bottom = screen_height - 50

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景
    screen.fill((0, 0, 0))

    # 绘制玛丽
    screen.blit(mario_image, mario_rect)

    # 更新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
```

请注意，这只是一个简单的示例代码，只包含了玛丽的静态图像和基本的游戏循环。如果你想要一个完整的超级玛丽游戏，需要更多的代码和资源。希望这个简单示例能帮到你入门。
