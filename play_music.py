import pygame

def play_mp3(audio):
    pygame.mixer.init()

    pygame.mixer.music.load(audio)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)