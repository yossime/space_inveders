import pygame
from shooting_spaceship import *
from sound import*
from display import*

# נתיב זמני - צריך להוסיף תמונת פולש
# original_image_invader = pygame.image.load("assets/invader.png")
# יצירת תמונת פולש זמנית
original_image_invader = pygame.Surface((50, 37))
original_image_invader.fill((255, 0, 0))  # אדום
pygame.draw.rect(original_image_invader, (150, 0, 0), (10, 10, 30, 17))  # מלבן כהה יותר
invaders_near = pygame.sprite.Group()
invaders_far = pygame.sprite.Group()
invaders_falling = pygame.sprite.Group()
rotation_angle = 4



class Inveder(pygame.sprite.Sprite):
    
    def __init__(self, x, y, original_image_inveders,direction):
        
        super().__init__()
        
        new_width = 50
        new_height = 37
        image_big = pygame.transform.scale(original_image_inveders, (new_width, new_height))
        image_small = pygame.transform.scale(original_image_inveders, (new_width//2, new_height//2))
        self.image_big = image_big
        self.image_small = image_small
        self.direction= direction
        if self.direction == 1:
             self.image = image_big
        else:
            self.image = image_small
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
           
    
    
    def change(self):
        if self.image == self.image_big:
            self.image = self.image_small
        else:
            self.image = self.image_big

    
    
    def update(self, shoot_spaceship_group ): 
        if self in invaders_far or self in invaders_near:
            self.rect.x += self.direction*5
        elif self in invaders_falling:
             # self.image =   pygame.transform.rotate(self.image, rotation_angle)
            self.rect.y += 15
       

       
             
                
                
        if self.rect.left >= window_width:
            invaders_near.remove(self)
            invaders_far.add(self)
            self.change()
            self.direction = self.direction * (-1)
            self.rect.y += 10

            

            

        if self.rect.right <= 0:
            invaders_near.add(self)
            invaders_far.remove(self)
            self.change()
            self.direction = self.direction * (-1)
            self.rect.y += 10

        
        if self  in invaders_near:
            if pygame.sprite.spritecollide(self, shoot_spaceship_group, True):
                invaders_falling.add(self)
                invaders_near.remove(self)
                        # self.kill()   
                        
        
        
        if len(invaders_far) == 0 and len(invaders_near) == 0:
            sound_manager.play_viktory_sound()


        
              
    
    
        

def grup_inveders():
    for j in range(2):
        for i in range(5):
            invaders_far.add(Inveder((i*75)+600, (j*100)+40, original_image_invader, -1))
            invaders_near.add(Inveder((i*75)+40, (j*100)+40, original_image_invader, 1))

           