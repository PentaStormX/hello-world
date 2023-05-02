# 1. 그냥 출력
print("Hello World~!")

# 2. 변수에 넣고 출력
a = "Hello World~!"
print(a)

# 3. 변수안의 string 갯수만큼 반복문 돌며 각각 출력하는데 end flag를 이용하여 띄어쓰기.
for x in a:
    print(x, end=" ")

# 4. pygame 모듈을 이용하여 윈도우에 문구 출력하기.
import pygame
import sys

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200

pygame.init()

SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

font = pygame.font.SysFont("arial", 30, True, True)
text = font.render("Hello World~!", True, (0, 0, 0))

while True:
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SURFACE.fill((255, 255, 255))

    SURFACE.blit(text, (SCREEN_WIDTH/3, SCREEN_HEIGHT/3))
    pygame.display.update()