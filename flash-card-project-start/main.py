from tkinter import *
import pandas
import random

current_card = {}
timer = ""
to_learn = []
BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("data/words_to_learn.csv") as file:
        data = pandas.read_csv(file)
        to_learn = data.to_dict(orient="records")

except FileNotFoundError:
    with open("data/french_words.csv") as file:
        data = pandas.read_csv(file)
        to_learn = data.to_dict(orient="records")


# -------SAVE YOUR PROGRESS ------ #
def remove_word():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


def flip_card():
    global timer, current_card
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# ----- CREATE NEW FLASH CARDS ------- #
def next_card():
    global timer, current_card, to_learn
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    timer = window.after(3000, flip_card)


# ------- INTERFACE -------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(height=526, width=800)
canvas.grid(column=0, row=0, columnspan=2)
timer = window.after(3000, flip_card)

# Images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Interface for card
card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons
wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)
right = Button(image=right_img, highlightthickness=0, command=remove_word)
right.grid(column=1, row=1)

next_card()
window.mainloop()
