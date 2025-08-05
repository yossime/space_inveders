"""
Particle System for Visual Effects
"""
import pygame
import random
import math
from config import PARTICLE_SETTINGS, COLORS


class Particle:
    """Single particle for effects"""
    def __init__(self, x, y, velocity_x, velocity_y, color, life, size=3):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.color = color
        self.life = life
        self.max_life = life
        self.size = size
        self.alive = True
    
    def update(self):
        """Update particle position and life"""
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.life -= 1
        
        # Add gravity effect
        self.velocity_y += 0.1
        
        # Fade effect
        alpha = int(255 * (self.life / self.max_life))
        self.color = (*self.color[:3], max(0, alpha))
        
        if self.life <= 0:
            self.alive = False
    
    def draw(self, screen):
        """Draw particle"""
        if self.alive:
            # Create surface with alpha for transparency
            particle_surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surf, self.color, (self.size, self.size), self.size)
            screen.blit(particle_surf, (int(self.x - self.size), int(self.y - self.size)))


class ParticleSystem:
    """Manages all particle effects"""
    def __init__(self):
        self.particles = []
    
    def create_explosion(self, x, y, intensity=1):
        """Create explosion effect"""
        settings = PARTICLE_SETTINGS['explosion']
        particle_count = int(settings['count'] * intensity)
        
        for _ in range(particle_count):
            # Random direction
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(*settings['speed_range'])
            
            velocity_x = math.cos(angle) * speed
            velocity_y = math.sin(angle) * speed
            
            color = random.choice(settings['colors'])
            life = random.randint(*settings['life_range'])
            size = random.randint(2, 5)
            
            particle = Particle(x, y, velocity_x, velocity_y, color, life, size)
            self.particles.append(particle)
    
    def create_trail(self, x, y, direction_x=0, direction_y=1):
        """Create trail effect"""
        settings = PARTICLE_SETTINGS['trail']
        
        for _ in range(settings['count']):
            # Add some randomness to trail direction
            velocity_x = direction_x + random.uniform(-1, 1)
            velocity_y = direction_y + random.uniform(-1, 1)
            
            color = random.choice(settings['colors'])
            life = random.randint(*settings['life_range'])
            size = random.randint(1, 3)
            
            particle = Particle(x, y, velocity_x, velocity_y, color, life, size)
            self.particles.append(particle)
    
    def create_powerup_effect(self, x, y, color):
        """Create power-up collection effect"""
        for _ in range(15):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 4)
            
            velocity_x = math.cos(angle) * speed
            velocity_y = math.sin(angle) * speed
            
            life = random.randint(20, 40)
            size = random.randint(2, 4)
            
            particle = Particle(x, y, velocity_x, velocity_y, color, life, size)
            self.particles.append(particle)
    
    def update(self):
        """Update all particles"""
        for particle in self.particles[:]:  # Use slice to avoid modification during iteration
            particle.update()
            if not particle.alive:
                self.particles.remove(particle)
    
    def draw(self, screen):
        """Draw all particles"""
        for particle in self.particles:
            particle.draw(screen)
    
    def clear(self):
        """Clear all particles"""
        self.particles.clear()


# Global particle system instance
particle_system = ParticleSystem()