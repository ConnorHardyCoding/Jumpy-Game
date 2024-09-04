# Game settings/options
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                (0, HEIGHT * 3 / 4, 100, 20),
                (WIDTH - 100, HEIGHT * 3 / 4, 100, 20),
                (125, HEIGHT - 350, WIDTH - 250, 20),
                (100, 100, 50, 20)]

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BGCOLOR = (129, 179, 187)
