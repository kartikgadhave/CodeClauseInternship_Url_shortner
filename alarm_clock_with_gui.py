import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pygame

def set_alarm():
    try:
        alarm_time = entry.get()
        alarm_hms = list(map(int, alarm_time.split(':')))
        if len(alarm_hms) != 3 or any(t < 0 for t in alarm_hms):
            raise ValueError("Invalid time format")
        alarm_seconds = alarm_hms[0] * 3600 + alarm_hms[1] * 60 + alarm_hms[2]
        countdown(alarm_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid time in the format HH:MM:SS")

def countdown(seconds):
    while seconds > 0:
        time_str = f"{seconds//3600:02}:{(seconds//60)%60:02}:{seconds%60:02}"
        time_label.config(text=time_str)
        time_label.update()
        time.sleep(1)
        seconds -= 1
    time_label.config(text="00:00:00")
    time_label.update()
    play_alarm()

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")  # Provide the path to your buzzer sound file
    pygame.mixer.music.play()

def reset_alarm():
    time_label.config(text="00:00:00")

def change_time_zone():
    # Implement the functionality to change time zone here
    pass

root = tk.Tk()
root.title("Alarm Clock by Kartik Gadhave")
root.geometry("400x250")

title_label = ttk.Label(root, text="Alarm Clock", font=("Arial", 16))
title_label.pack(pady=10)

entry_label = ttk.Label(root, text="Set Alarm (HH:MM:SS):")
entry_label.pack()

entry = ttk.Entry(root, width=20)
entry.pack()

set_button = ttk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

reset_button = ttk.Button(root, text="Reset", command=reset_alarm)
reset_button.pack()

time_zone_button = ttk.Button(root, text="Change Time Zone", command=change_time_zone)
time_zone_button.pack()

time_label = ttk.Label(root, text="00:00:00", font=("Arial", 24))
time_label.pack(pady=10)

root.mainloop()
