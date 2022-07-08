import pygame


class entity():
    entity_list = list()
    rect_list = list()

    def __init__(self, image, scale_size=1, start_pos=(0, 0), color_key=(121, 255, 121)):
        self.image_entity = pygame.image.load(image).convert()
        self.image_entity.set_colorkey((color_key))
        self.rectangle = self.image_entity.get_rect()
        self.image_entity = pygame.transform.scale(self.image_entity, (self.rectangle.width*scale_size, self.rectangle.height*scale_size))
        self.rectangle = self.image_entity.get_rect()
        self.rectangle.move_ip(start_pos)
        self.rect_list.append(self.rectangle)
        self.entity_list.append(self)


class GameObject(entity):

    def __init__(self, image, scale_size=1, start_pos=(0, 0), color_key=(121, 255, 121)):
        self.moving = {
            "up": False,
            "down": False,
            "right": False,
            "left": False,
        }
        self.collision_kind = {
            "top": False,
            "bottom": False,
            "right": False,
            "left": False,

        }
        super().__init__(image, scale_size, start_pos, color_key)

    def collision_test(self):
        self.hit_list = list()
        self.test_collision = list(self.rect_list)
        self.test_collision.remove(self.rectangle)

        for rect in self.test_collision:
            if self.rectangle.colliderect(rect):
                self.hit_list.append(rect)

        return self.hit_list

    def movement(self, x=0, y=0):
        self.collision_kind = {
            "top": False,
            "bottom": False,
            "right": False,
            "left": False,

        }
# moving in the X axis
        if x != 0:
            self.rectangle.move_ip(x, 0)
            self.hit_list = self.collision_test()
            for rect in self.hit_list:
                if x > 0:
                    self.rectangle.right = rect.left
                    self.collision_kind["right"] = True
                elif x < 0:
                    self.rectangle.left = rect.right
                    self.collision_kind["left"] = True

# moving in the Y axis
        if y != 0:
            self.rectangle.move_ip(0, y)
            self.hit_list = self.collision_test()
            for rect in self.hit_list:
                if y > 0:
                    self.rectangle.bottom = rect.top
                    self.collision_kind["bottom"] = True
                elif y < 0:
                    self.rectangle.top = rect.bottom
                    self.collision_kind["top"] = True


def map_generator(path, tiles, scale_size=1, color_key=(121, 255, 121)):
    file = open(path, 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    y = 0
    for row in data:
        x = 0
        for tile in list(row):
            if tile == "1":
                GameObject(tiles, scale_size, (x*16*scale_size, y*16*scale_size), color_key)
            x += 1
        y += 1




