from def_variable import *

pygame.init()
screen = pygame.display.set_mode((1600,1000))

selected = False
mouse_pressed = False
mouse_clicked = False

while run: # 와일문을 돌린다

    for event in pygame.event.get(): # 이벤트 반복문을 돌린다
        if event.type == pygame.QUIT: # X버튼을 눌렀다면
            run = False # 게임을 끝낸다

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP: # 마우스를 땠다면
            mx, my = pygame.mouse.get_pos()
            sp_num = mouse_target(Army_w, Army_h, (mx, my))
            if sp_num != -1:
                print(sp_num)

        elif event.type == KEYDOWN:
            if event.key == ord('f'):
                combat_detection()
                
    screen.blit(img_map, [0, 0]) # 배경 소환

    for a in range(Army_Count):
        screen.blit(img_Army, [Army_x[a], Army_y[a]]) # 군대 소환

    for a in range(enemy_Count):
        screen.blit(img_enemy, [enemy_x[a], enemy_y[a]]) # 적군 소환

    pygame.display.update() # 업데이트 한다