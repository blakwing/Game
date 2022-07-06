import pygame
import sys
from entities import entity, GameObject, map_generator
pygame.init()


clock = pygame.time.Clock()

window_size = (700, 500)

background = 95, 205, 228

screen = pygame.display.set_mode(window_size)
screen.fill(background)
pygame.display.flip()

second_guy = GameObject("chico.png", 2, (0, 0), (255, 255, 255))

map_generator("map1.txt", "Grass_Tile.png", 2)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("game quit!")
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                second_guy.moving["left"] = True

            if event.key == pygame.K_RIGHT:
                second_guy.moving["right"] = True

            if event.key == pygame.K_UP:
                second_guy.moving["up"] = True

            if event.key == pygame.K_DOWN:
                second_guy.moving["down"] = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                second_guy.moving["left"] = False

            if event.key == pygame.K_RIGHT:
                second_guy.moving["right"] = False

            if event.key == pygame.K_UP:
                second_guy.moving["up"] = False

            if event.key == pygame.K_DOWN:
                second_guy.moving["down"] = False

    second_guy.movement(0, 2)
    if second_guy.moving["left"]:
        second_guy.movement(-3)
    if second_guy.moving["right"]:
        second_guy.movement(3)
    if second_guy.moving["up"] and second_guy.collision_kind["bottom"]:
        second_guy.movement(0, -3)


    clock.tick(60)

    screen.fill(background)

    for i in entity.entity_list:
        screen.blit(i.image_entity, i.rectangle)

    pygame.display.update(entity.rect_list)
