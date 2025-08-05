
import pygame
from sound import*

pygame.init()




shoot_spaceship_group = pygame.sprite.Group()



class Shooting(pygame.sprite.Sprite):
    def __init__(self, point):
        super().__init__()
        
        # נתיב זמני - צריך להוסיף תמונת קליע של החללית
        # original_image_shooting = pygame.image.load("assets/spaceship_bullet.png")
        # יצירת תמונת קליע זמנית
        original_image_shooting = pygame.Surface((10, 20))
        original_image_shooting.fill((0, 255, 255))  # תכלת
        new_width_shooting = 30
        new_height_shooting = 60
        image_shooting = pygame.transform.scale(original_image_shooting, (new_width_shooting, new_height_shooting))
        
        self.image = image_shooting
        self.rect = self.image.get_rect()
        self.rect.center = point

    
    def update(self):
        
        self.rect.y -= 20
        if self.rect.y < 0:
             self.kill()
        

def shoot_new(point, counter,running_shoot, spaceship, sound_manager):
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and counter-running_shoot>20:
            object = Shooting(spaceship.rect.midtop,)
            shoot_spaceship_group.add(object)
            running_shoot=counter
            sound_manager.play_shoot_sound()
    
    return shoot_spaceship_group,running_shoot





