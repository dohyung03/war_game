from os import scandir
from main_variable import *


def check_point_in_rect(x,y, rect):
    if rect.top < y and rect.bottom > y:
        if rect.left < x and rect.right > x:
            return True
    return False

def combat_detection(): # 교전을 위한 피타고라스의 정의계산
    global enemy_x, enemy_y, enemy_w, enemy_h, enemy_Count
    global Existing_Army_x, Existing_Army_y, Army_h, Army_w
    for h in range(Army_Count):

        Existing_Army_x[h] = Existing_Army_x[h] + Army_w / 2
        Existing_Army_y[h] = Existing_Army_y[h] + Army_h / 2
        for z in range(enemy_Count):
            check_enemy_x = enemy_x[z] + enemy_w / 2
            check_enemy_y = enemy_y[z] + enemy_h / 2

        p1 = (Existing_Army_x[h], Existing_Army_y[h]) # 아군 중앙점
        p2 = (check_enemy_x, check_enemy_y) # 적군 중앙점

        p1_line = p1[0] - p2[0] # x선 구하기
        p2_line = p1[1] - p2[1] # y선 구하기

        line_check = math.sqrt((p1_line * p1_line) + (p2_line * p2_line)) # 제곱근 계산하기
        print(line_check)
        if line_check <= 150:
            print("전투 개시")


def mouse_target(w, h, pos): # 마우스 충돌감지

    global Army_do_you_see, Army_x, Army_y, Army_w, Army_h, first_click, Existing_Army_x, Existing_Army_y
    global first_X, first_Y, second_click, second_X, second_Y, first_click_Army

    for n in range(Army_Count):
        if Army_do_you_see[n] == True:

            army_rect = pygame.Rect(Army_x[n],Army_y[n], w, h)

            print(pos[0],pos[1])
            if check_point_in_rect(pos[0],pos[1], army_rect):
                if first_click == False and second_click == False:
                    first_click = True
                    first_click_Army = n
                    return n

            elif first_click == True and second_click == False:

                Army_x[n] = pos[0] - Army_w / 2
                Army_y[n] = pos[1] - Army_h / 2

                Existing_Army_x[n] = Army_x[n]
                Existing_Army_y[n] = Army_y[n]

                first_click = False

    return -1