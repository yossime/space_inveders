"""
Power-up System
"""
import pygame
import random
import math
from config import POWERUP_TYPES, COLORS


class PowerUp(pygame.sprite.Sprite):
    """Power-up item that falls from destroyed invaders"""
    def __init__(self, x, y, powerup_type):
        super().__init__()
        self.powerup_type = powerup_type
        self.config = POWERUP_TYPES[powerup_type]
        
        # Create visual representation
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Animation properties
        self.float_offset = 0
        self.rotation = 0
        self.pulse_size = 1.0
        
        # Movement
        self.speed = 2
        
        self.create_visual()
    
    def create_visual(self):
        """Create the visual representation of the power-up"""
        color = self.config['color']
        
        # Clear surface
        self.image.fill((0, 0, 0, 0))
        
        if self.powerup_type == 'RAPID_FIRE':
            # Draw bullets symbol
            for i in range(3):
                pygame.draw.circle(self.image, color, (10 + i * 5, 15), 3)
        
        elif self.powerup_type == 'SHIELD':
            # Draw shield symbol
            points = [(15, 5), (25, 15), (15, 25), (5, 15)]
            pygame.draw.polygon(self.image, color, points)
            pygame.draw.polygon(self.image, COLORS['WHITE'], points, 2)
        
        elif self.powerup_type == 'MULTI_SHOT':
            # Draw spread pattern
            center = (15, 15)
            for angle in [-30, 0, 30]:
                end_x = center[0] + math.cos(math.radians(angle)) * 10
                end_y = center[1] + math.sin(math.radians(angle)) * 10
                pygame.draw.line(self.image, color, center, (end_x, end_y), 3)
        
        elif self.powerup_type == 'LASER':
            # Draw laser beam
            pygame.draw.rect(self.image, color, (12, 5, 6, 20))
            pygame.draw.circle(self.image, COLORS['WHITE'], (15, 15), 8, 2)
    
    def update(self):
        """Update power-up animation and movement"""
        # Move down
        self.rect.y += self.speed
        
        # Floating animation
        self.float_offset += 0.2
        float_y = math.sin(self.float_offset) * 3
        
        # Rotation animation
        self.rotation += 3
        
        # Pulse animation
        self.pulse_size = 1.0 + math.sin(self.float_offset * 2) * 0.2
        
        # Recreate visual with animations
        self.create_visual()
        
        # Apply transformations
        if self.rotation != 0:
            self.image = pygame.transform.rotate(self.image, self.rotation)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        
        # Remove if off screen
        if self.rect.top > 850:  # Screen height + margin
            self.kill()


class PowerUpManager:
    """Manages all power-ups and their effects"""
    def __init__(self):
        self.powerups = pygame.sprite.Group()
        self.active_effects = {}
        
    def spawn_powerup(self, x, y, chance=0.15):
        """Spawn a random power-up with given chance"""
        if random.random() < chance:
            powerup_type = random.choice(list(POWERUP_TYPES.keys()))
            powerup = PowerUp(x, y, powerup_type)
            self.powerups.add(powerup)
    
    def check_collection(self, spaceship_rect):
        """Check if spaceship collected any power-ups"""
        collected = []
        for powerup in self.powerups:
            if powerup.rect.colliderect(spaceship_rect):
                collected.append(powerup.powerup_type)
                powerup.kill()
        return collected
    
    def activate_powerup(self, powerup_type):
        """Activate a power-up effect"""
        duration = POWERUP_TYPES[powerup_type]['duration']
        self.active_effects[powerup_type] = pygame.time.get_ticks() + duration
    
    def is_active(self, powerup_type):
        """Check if a power-up is currently active"""
        if powerup_type in self.active_effects:
            return pygame.time.get_ticks() < self.active_effects[powerup_type]
        return False
    
    def get_active_effects(self):
        """Get list of currently active effects"""
        current_time = pygame.time.get_ticks()
        active = []
        
        for effect, end_time in list(self.active_effects.items()):
            if current_time < end_time:
                active.append(effect)
            else:
                del self.active_effects[effect]
        
        return active
    
    def update(self):
        """Update all power-ups"""
        self.powerups.update()
    
    def draw(self, screen):
        """Draw all power-ups"""
        self.powerups.draw(screen)
    
    def clear(self):
        """Clear all power-ups"""
        self.powerups.empty()
        self.active_effects.clear()


# Global power-up manager instance
powerup_manager = PowerUpManager()