import os
import pygame

pygame.init()

songs_folder = "songs"
playlist = [f for f in os.listdir(songs_folder) if f.endswith("mp3")]
if not playlist:
    print("put some music in here songs/ first")
    exit()

current_index = 0

def playSong(index):
    pygame.mixer.music.load(os.path.join(songs_folder, playlist[index]))
    pygame.mixer.music.play()
    print(f"Now playing: {playlist[index]}")

def pauseSong():
    pygame.mixer.music.pause()
    print("Paused")
