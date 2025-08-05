import pygame
class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        # נתיבים זמניים - צריך להוסיף קבצי שמע
        # self.shoot_sound = pygame.mixer.Sound("assets/shoot.mp3")
        # self.explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
        # self.game_over_sound = pygame.mixer.Sound("assets/game_over.mp3")
        # self.viktory_sound = pygame.mixer.Sound("assets/victory.mp3")
        # pygame.mixer.music.load("assets/background_music.mp3")
        
        # צלילים זמניים - ללא קבצי שמע
        self.shoot_sound = None
        self.explosion_sound = None
        self.game_over_sound = None
        self.viktory_sound = None
        
    def play_shoot_sound(self):
        if self.shoot_sound:
            self.shoot_sound.play()
        
    def play_explosion_sound(self):
        if self.explosion_sound:
            self.explosion_sound.play()
        
    def play_game_over_sound(self):
        if self.game_over_sound:
            self.game_over_sound.play()

    def play_viktory_sound(self):
        if self.viktory_sound:
            self.viktory_sound.play()
    
    def play_background_music(self):
        try:
            pygame.mixer.music.play(-1)
        except:
            pass  # אם אין מוזיקת רקע, פשוט נמשיך


sound_manager = SoundManager()        