import pygame

#initializing the mixer
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Digital Music Creation\second_melody.mid")
pygame.mixer.music.play()

# keep the script running to play the track
input("Press Enter to stop playback...")
pygame.mixer.music.stop()