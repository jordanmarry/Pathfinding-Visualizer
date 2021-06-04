import pygame
pygame.init()

#
#
# Screen Settings
#
#

WIDTH = 1200
HEIGHT = 768

GRID_WIDTH = WIDTH - 240 - 24*2
GRID_HEIGHT = HEIGHT - 24*2

#
#
# Colors
#
#

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (60, 150, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
INDIGO = (75,0,130)

#
# 
# Grid Settings
# 
# 

# GS - Grid-Start

GS_X = 0
GS_Y = 0
# GE - Grid-End

GE_X = 1200
GE_Y = 600

#
# 
# Algo Button Length and Positions
# 
# 

ALGO_BUTTON_LENGTH = 200
ALGO_BUTTON_HEIGHT = 20

ALGO_BUTTON_POSX = 20
ALGO_BUTTON_POSY = 640