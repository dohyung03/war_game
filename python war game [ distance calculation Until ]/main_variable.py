from platform import node
import pygame
import sys
import math
import ctypes
import random
from pygame.locals import *

# 지역 코드 및 지역에 있는 정보
# 0 = 지역의 성질 1 = 현재 지역에 군대가 있는가? (T or F) 2 = 적군이 존재하는가? (T or F) 3 = 지역의 X,Y
# (1 = 평지 2 = 도시 3 = 숲 4 = 산 5 = 강)
run = True
if run:
    A1 = [1, 1, 0, [0, 0]]
    A2 = [1, 1, 0, [320, 0]]
    A3 = [5, 1, 0, [640, 0]]
    A4 = [3, 1, 0, [960, 0]]
    A5 = [1, 1, 0, [1280, 0]]
    A6 = [1, 1, 0, [0, 250]]
    A7 = [3, 1, 0, [320, 250]]
    A8 = [2, 1, 0, [640, 250]]
    A9 = [3, 1, 0, [960, 250]]
    A0 = [1, 1, 0, [1280, 250]]
    B1 = [3, 1, 0, [0, 500]]
    B2 = [2, 1, 0, [320, 500]]
    B3 = [2, 1, 0, [640, 500]]
    B4 = [3, 1, 0, [960, 500]]
    B5 = [1, 1, 0, [1280, 500]]
    B6 = [1, 1, 0, [0, 750]]
    B7 = [1, 1, 0, [320, 750]]
    B8 = [5, 1, 0, [640, 750]]
    B9 = [3, 1, 0, [960, 750]]
    B0 = [1, 1, 0, [1280, 750]]

map_list = [
    [A1,A2,A3,A4,A5,
     A6,A7,A8,A9,A0,
     B1,B2,B3,B4,B5,
     B6,B7,B8,B9,B0]
]

map_w = 1600
map_h = 1000
map_feet_w = 320
map_feet_h = 250
map_nm = 0
map1_nm = 20
img_map = pygame.image.load("map.png") # 지도 이미지
img_map = pygame.transform.scale(img_map,(map_w, map_h)) # 지도 크기 조절

Army_Count = 1
Army_x = [500] * Army_Count # 아군 X
Army_y = [500] * Army_Count # 적군 Y
Existing_Army_x = [500] * Army_Count
Existing_Army_y = [500] * Army_Count
Army_do_you_see = [True] * Army_Count
Army_w = 100 # 군인 폭
Army_h = 100 # 군인 높이
img_Army = pygame.image.load("Ukrainian Army.png") # 군대 이미지
img_Army = pygame.transform.scale(img_Army,(Army_w, Army_h)) # 군대 크기 조절

enemy_Count = 1
enemy_x = [random.randrange(0,1600)] * enemy_Count
enemy_y = [random.randrange(0,1000)] * enemy_Count
check_enemy_x = 0
check_enemy_y = 0
enemy_do_you_see = [True] * enemy_Count
enemy_w = 100 # 적군 폭
enemy_h = 100 # 적군 높이
img_enemy = pygame.image.load("Russian Army.png") # 군대 이미지
img_enemy = pygame.transform.scale(img_enemy,(enemy_w, enemy_h)) # 군대 크기 조절
first_click = False
first_X = None
first_Y = None

second_click = False
second_X = None
second_Y = None
first_click_Army = -1