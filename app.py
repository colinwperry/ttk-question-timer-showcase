from tkinter import *
from tkinter import ttk
import time 

root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

timer_length = 120 # in seconds

def timerStart():
    global start_time; start_time = time.time()
    global timer_length; timer_length = 120
    timer_button.configure(text="Stop Timer", command=timerStop)
    root.after(0, incrementTimer)

def timerStop():
    global timer_length; timer_length = 0
    timer_label.configure(text="0:00")
    timer_button.configure(text="Start Timer", command=timerStart)

def incrementTimer():
    if timer_length > 0:
        root.after(1000, incrementTimer)
        proper_time = int(start_time - time.time() + timer_length)
        minute, second = proper_time // 60, proper_time % 60
        timer_label.configure(text=f"{minute}:{second:02}") 

timer_label = ttk.Label(frame, text="0:00")
timer_label.grid(column=0, row=0)

timer_button = ttk.Button(frame, text="Start Timer", command=timerStart)
timer_button.grid(column=0, row=1)

root.mainloop()
