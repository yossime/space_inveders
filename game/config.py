"""
Game Configuration Settings
"""

# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors (RGB)
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'PURPLE': (128, 0, 128),
    'ORANGE': (255, 165, 0),
    'CYAN': (0, 255, 255),
    'DARK_BLUE': (0, 0, 50),
    'NEON_GREEN': (57, 255, 20),
    'NEON_BLUE': (4, 217, 255),
    'LASER_RED': (255, 50, 50),
    'EXPLOSION_ORANGE': (255, 100, 0)
}

# Game settings
SPACESHIP_SPEED = 8
BULLET_SPEED = 12
INVADER_SPEED = 2
INVADER_DROP_SPEED = 40

# Difficulty progression
DIFFICULTY_LEVELS = {
    1: {'invader_speed': 1, 'bullet_frequency': 0.02, 'invader_count': 35},
    2: {'invader_speed': 1.5, 'bullet_frequency': 0.03, 'invader_count': 40},
    3: {'invader_speed': 2, 'bullet_frequency': 0.04, 'invader_count': 45},
    4: {'invader_speed': 2.5, 'bullet_frequency': 0.05, 'invader_count': 50},
    5: {'invader_speed': 3, 'bullet_frequency': 0.06, 'invader_count': 55}
}

# Power-ups
POWERUP_TYPES = {
    'RAPID_FIRE': {'duration': 5000, 'color': COLORS['YELLOW']},
    'SHIELD': {'duration': 8000, 'color': COLORS['CYAN']},
    'MULTI_SHOT': {'duration': 6000, 'color': COLORS['PURPLE']},
    'LASER': {'duration': 4000, 'color': COLORS['NEON_GREEN']}
}

# Particle effects
PARTICLE_SETTINGS = {
    'explosion': {
        'count': 20,
        'speed_range': (2, 8),
        'life_range': (30, 60),
        'colors': [COLORS['EXPLOSION_ORANGE'], COLORS['RED'], COLORS['YELLOW']]
    },
    'trail': {
        'count': 5,
        'speed_range': (1, 3),
        'life_range': (10, 20),
        'colors': [COLORS['NEON_BLUE'], COLORS['CYAN']]
    }
}