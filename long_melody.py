import pygame


pygame.mixer.init()
pygame.mixer.music.load(r"C:\Digital Music Creation\longer_melody")
pygame.mixer.music.play()

input("Press enter to stop playback...")
pygame.mixer.music.stop()