"""
Space Invaders Game - Main Game Loop
"""
import pygame
import baise
import sound
import inveders


def main():
    """Main game function"""
    # Initialize pygame
    pygame.init()
    
    # Game variables
    running_shoot = 0
    running_shoot_inveders = 0
    counter = 0
    running = True
    
    # Game clock
    clock = pygame.time.Clock()
    dt = 0
    
    # Start background music and create invaders
    sound.sound_manager.play_background_music()
    inveders.grup_inveders()
    
    # Main game loop
    while running:
        counter += 1
        
        # Handle game conditions
        shoot_inveders_group, shoot_spaceship_group, running, running_shoot_inveders, running_shoot, running = baise.check_condition(
            counter, running_shoot, running_shoot_inveders, running
        )
        
        # Update and draw game
        baise.show()
        baise.updates()
        
        # Update display
        pygame.display.flip()
        dt = clock.tick(60) / 100
    
    # Cleanup
    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()