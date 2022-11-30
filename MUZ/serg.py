import pygame
from gtts import gTTS




audio = "audio.mp3"
language = "ru"
sp = gTTS(text="Сергей", lang=language, slow=False)
sp.save(audio)


pygame.init()
song = pygame.mixer.Sound(audio)
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(60)
pygame.quit()