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

def nextSong():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    playSong(current_index)

def prevSong():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    playSong(current_index)

while True:
    command = input("Command (play/pause/next/prev/quit): ").lower()
    if command == "play":
        playSong(current_index)
    elif command == "pause":
        pauseSong()
    elif command == "next":
        nextSong()
    elif command == "prev":
        prevSong()
    elif command == "quit":
        pygame.mixer.music.stop()
        break
    else:
        print("Unknown command :(")
        
