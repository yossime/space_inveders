import pygame
from pygame.locals import *
from spaceship import*
from inveders import*
from shooting_spaceship import*
from shooting_inveders import*
from sound import*
from display import*







WHITE = (255, 255, 255)




def check_condition(counter, running_shoot, running_shoot_inveders, running):
    
        shoot_spaceship_group, running_shoot = shoot_new(spaceship.rect.midtop, counter, running_shoot, spaceship , sound_manager)
        shoot_inveders_group, running_shoot_inveders = shoot_inveders_new(counter, running_shoot_inveders, invaders_near) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  

        if spaceship.life <= 0:
           
            game_surface ,game_rect = game_over_condition()
            window.blit(game_surface, game_rect)
            sound_manager.play_game_over_sound()
        
        return    shoot_inveders_group ,shoot_spaceship_group, running, running_shoot_inveders, running_shoot, running, 





def life_condition(spaceship):
        
        font = pygame.font.Font(None, 50)
        
        life_surface = font.render(f"life:{spaceship.life}", True, WHITE)
        life_rect = life_surface.get_rect()
        life_rect.center = (80, window_height - 50)
        return life_surface ,life_rect



def game_over_condition():
        font = pygame.font.Font(None, 200)
        game_surface = font.render("game over", True, (225,0,0))
        game_rect = game_surface.get_rect()
        game_rect.center = (window_width//2, window_height//2)
        return game_surface ,game_rect
        


def updates():
        
        invaders_near.update(shoot_spaceship_group )
        invaders_far.update(shoot_spaceship_group )
        invaders_falling.update(shoot_spaceship_group )
        shoot_spaceship_group.update()
        spaceship.update(shoot_inveders_group, sound_manager)
        shoot_inveders_group.update()        



def show():
        
        life_surface, life_rect = life_condition(spaceship)
        window.blit(resized_image_beckgrand, (0,0)) 
        invaders_far.draw(window)
        invaders_near.draw(window)
        invaders_falling.draw(window)
        shoot_spaceship_group.draw(window)
        shoot_inveders_group.draw(window)
        window.blit(life_surface, life_rect)
        window.blit(spaceship.image, spaceship.rect)        

