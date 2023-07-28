import os
import tkinter as tk
from tkinter import filedialog
import pygame

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        playlist.append(file_path)
        song = os.path.basename(file_path)
        song_listbox.insert(tk.END, song)

def play_music():
    if not playlist:
        return
    global current_song_index
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_music()

def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Initialize pygame
pygame.mixer.init()

# Variables
playlist = []
current_song_index = 0

# Playlist Listbox
song_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
song_listbox.pack()

# Buttons
btn_play = tk.Button(root, text="Play", command=play_music)
btn_play.pack(side=tk.LEFT)

btn_pause = tk.Button(root, text="Pause", command=pause_music)
btn_pause.pack(side=tk.LEFT)

btn_unpause = tk.Button(root, text="Unpause", command=unpause_music)
btn_unpause.pack(side=tk.LEFT)

btn_stop = tk.Button(root, text="Stop", command=stop_music)
btn_stop.pack(side=tk.LEFT)

btn_prev = tk.Button(root, text="Prev", command=prev_song)
btn_prev.pack(side=tk.LEFT)

btn_next = tk.Button(root, text="Next", command=next_song)
btn_next.pack(side=tk.LEFT)

btn_choose = tk.Button(root, text="Choose Song", command=choose_file)
btn_choose.pack()

# Volume Scale
volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(70)
volume_scale.pack()

# Run the main loop
root.mainloop()
