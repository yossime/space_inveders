import pygame

pygame.init()
window_width = 1000
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Object and Group Example")


# נתיב זמני - צריך להוסיף תמונת רקע
# original_image_beckgrand = pygame.image.load("assets/background.jpg")
# יצירת רקע צבעוני זמני
original_image_beckgrand = pygame.Surface((1000, 600))
original_image_beckgrand.fill((0, 0, 50))  # כחול כהה
new_width_beckgrand = window_width
new_height_beckgrand= window_height
resized_image_beckgrand = pygame.transform.scale(
    original_image_beckgrand, (new_width_beckgrand, new_height_beckgrand))