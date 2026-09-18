from tkinter import *
from tkinter import ttk
import time 

root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

timer_label = ttk.Label(frame, text="0:00")
timer_label.grid(column=0, row=0)

question_container = {
        1: ["What is a variable?", "A way to save and use information."],
        2: ["print(\"Hello World!\")", "prints Hello World!"]
        }

logic_question_button = ttk.Button(frame, text="Logic Question", command=lambda: questionStart(1))
logic_question_button.grid(column=0, row=1)

code_question_button = ttk.Button(frame, text="Code Question", command=lambda: questionStart(2))
code_question_button.grid(column=1,row=1)

def questionStart(question_id):
    print(question_container[question_id][0])

def timerStart():
    global start_time; start_time = time.time()
    global timer_length; timer_length = 120
    timer_button.configure(text="Stop Timer", command=timerStop)
    incrementTimer()

def timerStop():
    global timer_length; timer_length = 0
    timer_button.configure(text="Start Timer", command=timerStart)

def incrementTimer():
    if timer_length > 0:
        root.after(1000, incrementTimer)
        proper_time = int(start_time - time.time() + timer_length)
        minute, second = proper_time // 60, proper_time % 60
        timer_label.configure(text=f"{minute}:{second:02}") 

root.mainloop()
