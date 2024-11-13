import pygame

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Digital Music Creation\third_melody.mid")
pygame.mixer.music.play()

input("Press Enter to stop playback...")
pygame.mixer.music.stop()