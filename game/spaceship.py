
import pygame
from sound import*
from display import*



# נתיב זמני - צריך להוסיף תמונת חללית
# original_image_spaceship = pygame.image.load("assets/spaceship.png")
# יצירת תמונת חללית זמנית
original_image_spaceship = pygame.Surface((130, 100))
original_image_spaceship.fill((255, 255, 255))  # לבן
pygame.draw.polygon(original_image_spaceship, (0, 255, 0), [(65, 10), (20, 90), (110, 90)])  # משולש ירוק
New_width = 130
New_height = 100


class Spaceship(pygame.sprite.Sprite):
    
    def __init__(self, x, y, original_image_spaceship,):
        super().__init__()
        self.image= pygame.transform.scale(original_image_spaceship, (New_width, New_height))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.life = 5

    
    def update(self, shoot_invader_group, sound_manager):
        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 20
        if keys[pygame.K_RIGHT] and self.rect.right < window_width:
            self.rect.x += 20
        if pygame.sprite.spritecollide(self, shoot_invader_group, True, pygame.sprite.collide_mask):
                self.life -= 1
                sound_manager.play_explosion_sound()
                
                      

spaceship = Spaceship(window_width//2, window_height -New_height, original_image_spaceship)