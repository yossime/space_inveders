import pygame
import random



# נתיב זמני - צריך להוסיף תמונת קליע
# original_invader_shooting = pygame.image.load("assets/invader_bullet.png")
# יצירת תמונת קליע זמנית
original_invader_shooting = pygame.Surface((20, 30))
original_invader_shooting.fill((255, 100, 0))  # כתום
new_width = 20
new_height = 30
shoot_invader_image = pygame.transform.scale(original_invader_shooting, (new_width, new_height))

shoot_inveders_group= pygame.sprite.Group()

class Shooting_inveders(pygame.sprite.Sprite):
    def __init__(self, point):
        super().__init__()
        
        self.image = shoot_invader_image
        self.rect = self.image.get_rect()
        self.rect.center = point

    def update(self):
        
        self.rect.y += 5
        if self.rect.y > 1000:
            self.kill()

def shoot_inveders_new( counter, running_shoot_inveders, invaders_near):
    
    if counter - running_shoot_inveders > 30:
        while   len(invaders_near) > 0:
            inveder = random.choice(invaders_near.sprites())
            object = Shooting_inveders(inveder.rect.midbottom)
            shoot_inveders_group.add(object)

            running_shoot_inveders = counter
            
            return shoot_inveders_group, running_shoot_inveders
    
    return shoot_inveders_group, running_shoot_inveders