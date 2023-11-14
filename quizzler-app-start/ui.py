from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        # Canvas
        self.q_canvas = Canvas(height=250, width=300)
        self.q_text = self.q_canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), width=280)
        self.q_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Buttons
        t_image = PhotoImage(file="images/true.png")
        f_image = PhotoImage(file="images/false.png")
        self.t_button = Button(image=t_image, highlightthickness=0, command=self.true_pressed)
        self.t_button.grid(row=2, column=0, padx=20, pady=20)
        self.f_button = Button(image=f_image, highlightthickness=0, command=self.false_pressed)
        self.f_button.grid(row=2, column=1, padx=20, pady=20)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.q_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.q_canvas.itemconfig(self.q_text, text=question)
        else:
            self.q_canvas.itemconfig(self.q_text, text="End of Quiz.")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.q_canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.q_canvas.config(bg="red")
        self.window.after(1000, self.next_question)
