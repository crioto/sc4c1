import pygame

# 1. Добавить свойство класса - скорость перемещения
# self.movement_speed
# 2. Создать несколько видов анимации и переключаться между ними
# по кнопке
# 2.a Расширить свойства swimming и climbing загрузкой анимации
# 2.b В функции update_animation проверять тип анимации и проигрывать
# соответствующую
# 2.c По нажатию кнопки менять анимацию

class Character():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        fpath = 'character/PNG/Adventurer/Poses'
        self.walking = [pygame.image.load(fpath+'/adventurer_walk1.png'),
            pygame.image.load(fpath+'/adventurer_walk2.png')]
        self.swimming = []
        self.clibming = []
        self.step = 0
        self.anim = "walking"

    def update_animation(self):
        if self.step > 1:
            self.step = 0
        self.screen.blit(self.walking[self.step], (self.x, self.y))
        self.step += 1
        self.x += 1

    def set_animation(self, animation):
        self.anim = animation


def start():
    pygame.init()

    screen = pygame.display.set_mode((720, 480))

    char0 = Character(screen, 0, 100)
    char1 = Character(screen, 0, 200)
    char2 = Character(screen, 0, 300)

    FPS = pygame.time.Clock()

# Background
    bg = pygame.image.load('bg.png')

# Red Green Blue
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.draw.line(screen, BLUE, (150,130), (130,170))
    pygame.draw.line(screen, BLUE, (150,130), (170,170))
    pygame.draw.line(screen, GREEN, (130,170), (170,170))
    pygame.draw.circle(screen, WHITE, (100,50), 30)
    pygame.draw.circle(screen, WHITE, (200,50), 30)
    pygame.draw.rect(screen, RED, (100, 200, 100, 50), 2)
    pygame.draw.rect(screen, WHITE, (110, 260, 80, 5))

    running = True
    while running:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        char0.update_animation()
        char1.update_animation()
        char2.update_animation()
        FPS.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
        if keys[pygame.L_a]:
            char0.set_animation("walking")
        pygame.display.update()

if __name__ == "__main__":
    start()
