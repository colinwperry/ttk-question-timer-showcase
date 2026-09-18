from tkinter import *
from tkinter import ttk
import time 

root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

timer_label = ttk.Label(frame, text="0:00")
timer_label.grid(column=0, row=0)

# each question has a UID, the first digit is the question number, and the second digit tells the program
# if the question is a code or logic comprehension question
question_dict = {
        "Question 1": ["What is a variable?", "A way to save and use information."],
        "Question 2": ["print(\"Hello World!\")", "prints Hello World!"]
        }

question_one_button = ttk.Button(frame, text="Question 1", command=lambda: questionStart(question_one_button, False))
question_one_button.grid(column=0, row=1)

question_two_button = ttk.Button(frame, text="Question 2", command=lambda: questionStart(question_two_button, True))
question_two_button.grid(column=1,row=1)

def questionStart(button, is_image_question):
    global question_answered; question_answered = False
    global timer_length
    timer_length = 120 if is_image_question else 60
    button.configure(text=question_dict[button["text"]][0], command=lambda: questionAnswered(button))
    # no visible difference, but ensures question changes before timer starts
    global start_time; start_time = time.time()
    incrementTimer()    

def questionAnswered(button):
    global question_answered; question_answered = True
    for key in question_dict:
        if button["text"] in question_dict[key]:
            button.configure(text=question_dict[key][1])

def incrementTimer():
    global question_answered
    if timer_length > 0 and not question_answered:
        proper_time = int(start_time - time.time() + timer_length)
        if proper_time <= 0:
            timer_label.configure(text="Times Up!")
            return
        root.after(1000, incrementTimer)
        minute, second = proper_time // 60, proper_time % 60
        timer_label.configure(text=f"{minute}:{second:02}") 

root.mainloop()
