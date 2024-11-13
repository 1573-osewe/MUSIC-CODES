import pygame


#initialize the mixer
pygame.mixer.init()
pygame.mixer.music.load(r"c:\Digital Music Creation\simple_melody.mid")
pygame.mixer.music.play()


# keep the script running to let the music play
input("Press Enter to stop playback...")
pygame.mixer.music.stop()



