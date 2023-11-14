import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ------------------------ TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    checkMark.config(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    global reps

    reps += 1
    if reps % 8 == 0:
        time = long_sec
        count_down(10)
        label.config(text="Long Break", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)

    elif reps % 2 == 1:
        time = work_sec
        count_down(5)
        label.config(text="Work", font=(FONT_NAME, 35, "normal"), fg=RED, bg=YELLOW)
    else:
        time = short_sec
        count_down(2)
        label.config(text="Short Break", font=(FONT_NAME, 35, "normal"), fg=PINK, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    minutes_count = count // 60
    seconds_remain = count % 60
    if seconds_remain < 10:
        seconds_remain = f"0{seconds_remain}"
    canvas.itemconfig(timer_text, text=f"{minutes_count}:{seconds_remain}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps//2
        for i in range(work_sessions):
            mark += "✔"
        checkMark.config(text=mark, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg= YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=2, row=2)

checkMark = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)

window.mainloop()

