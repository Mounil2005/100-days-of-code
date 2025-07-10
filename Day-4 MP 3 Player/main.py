import tkinter as tk
from tkinter import filedialog,ttk
import pygame
import os
from mutagen.mp3 import MP3

pygame.mixer.init()

root=tk.Tk()
root.title("MP3 PLayer")
root.geometry("400x300")
root.configure(bg="#E3F2FD")

is_paused=False
current_song=""
song_length=0

def pause_music():
    global is_paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_paused=True

def resume_music():
    global is_paused
    if is_paused: 
        pygame.mixer.music.unpause()
        is_paused=False
        update_progress() 

def stop_music():
    pygame.mixer.music.stop()
    progress_bar.set(0)
    current_time_label.config(text="0:00")

def set_volume(val):
    volume=float(val)
    pygame.mixer.music.set_volume(volume)


def browse_file():
    global current_song
    file_path=filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        current_song=file_path
        song_name=os.path.basename(file_path)
        song_label.config(text=f"Now Playing: {song_name}")
        audio = MP3(file_path)
        song_length = int(audio.info.length)
        total_time_label.config(text=f"Total: {format_time(song_length)}")
        play_music()

def play_music():
    if current_song:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volume_slider.get())
        update_progress()

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{int(mins)}:{int(secs):02}"

def update_progress():
    if pygame.mixer.music.get_busy():
        pos = pygame.mixer.music.get_pos() // 1000
        progress_bar.set(pos)
        current_time_label.config(text=format_time(pos))
        root.after(1000, update_progress)



# song_label=tk.Label(root, text="Welcome to MP3 Player", bg="#E3F2FD", font=("Arial", 14))
# song_label.pack(pady=20)

# btn_style = {"bg": "#1976D2", "fg": "white", "font": ("Arial", 12), "width": 15}

btn_style = {"bg": "#4F46E5", "fg": "white", "font": ("Arial", 12), "width": 15, "activebackground": "#4338CA"}



header = tk.Label(root, text="🎧 Welcome to my MP3 Player, Hope you like it!", bg="#F3F4F6", fg="#374151", font=("Helvetica", 16, "bold"))
header.pack(pady=10)

frame = tk.Frame(root, bg="#E5E7EB", bd=2, relief="ridge", padx=20, pady=20)
frame.pack(padx=20, pady=20)

song_label = tk.Label(frame, text="No song selected", bg="#E5E7EB", fg="#1F2937", font=("Arial", 12), wraplength=250)
song_label.pack(pady=10)

controls_frame = tk.Frame(frame, bg="#E5E7EB")
controls_frame.pack(pady=10)

time_frame = tk.Frame(frame, bg="#E5E7EB")
time_frame.pack()

current_time_label = tk.Label(time_frame, text="0:00", font=("Arial", 10), bg="#E5E7EB")
current_time_label.grid(row=0, column=0, padx=5)

progress_bar = ttk.Scale(time_frame, from_=0, to=100, orient='horizontal', length=200)
progress_bar.grid(row=0, column=1)

total_time_label = tk.Label(time_frame, text="Total: 0:00", font=("Arial", 10), bg="#E5E7EB")
total_time_label.grid(row=0, column=2, padx=5)

tk.Button(controls_frame, text="Play ▶️", command=play_music, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(controls_frame, text="Pause ⏸", command=pause_music, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(controls_frame, text="Resume ⏯", command=resume_music, **btn_style).grid(row=0, column=2, padx=5)
tk.Button(controls_frame, text="Stop ⏹", command=stop_music, **btn_style).grid(row=0, column=3, padx=5)


browse=tk.Button(frame, text="Choose .mp3 file", command=browse_file, **btn_style)
browse.pack(pady=10)

tk.Label(frame, text="🔊 Volume", bg="#E5E7EB", font=("Arial", 12)).pack()
volume_slider=tk.Scale(frame, from_=0, to=1, resolution=0.1, orient="horizontal", command=set_volume, bg="#E5E5EB")

volume_slider.set(0.5)
volume_slider.pack(pady=5)


# tk.Button(frame, text="Browse MP3", command=browse_file, **btn_style).pack(pady=5)
# tk.Button(frame, text="Play", command=play_music, **btn_style).pack(pady=5)
# tk.Button(frame, text="Pause", command=pause_music, **btn_style).pack(pady=5)
# tk.Button(frame, text="Resume", command=resume_music, **btn_style).pack(pady=5)
# tk.Button(frame, text="Stop", command=stop_music, **btn_style).pack(pady=5)

# play=tk.Button(root, text="Play", command=play_music, **btn_style)
# play.pack(pady=10)

# pause = tk.Button(root, text="Pause", command=pause_music, **btn_style)
# pause.pack(pady=5)

# resume = tk.Button(root, text="Resume", command=resume_music, **btn_style)
# resume.pack(pady=5)

# stop = tk.Button(root, text="Stop", command=stop_music, **btn_style)
# stop.pack(pady=5)

root.mainloop()