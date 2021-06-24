from tkinter import *
from quiz_brain import QuizBrain
from game_status import GameStatus

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.game_status: GameStatus = GameStatus.IN_PROGRESS
        self.feedback_in_progress = False

        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="QUESTION", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.feedback_in_progress = False
        self.canvas.config(bg="white")

        if not self.quiz.still_has_questions():
            self.game_status = GameStatus.GAME_OVER
            self.canvas.itemconfig(self.question_text, text="You've completed the quizGame" +
                                                            f"Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            return
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def false_pressed(self):
        if self.game_status == GameStatus.PLAY_AGAIN:
            self.window.quit()
            return
        elif self.game_status == GameStatus.GAME_OVER:
            self.prompt_play_again()
        else:
            if self.feedback_in_progress:
                return
            self.give_feedback(self.quiz.check_answer("false"))

    def true_pressed(self):
        if self.game_status == GameStatus.PLAY_AGAIN:
            self.quiz.start_new_game()
            self.game_status = GameStatus.IN_PROGRESS
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.get_next_question()
            return
        elif self.game_status == GameStatus.GAME_OVER:
            self.prompt_play_again()
        else:
            if self.feedback_in_progress:
                return
            self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right: bool):
        self.feedback_in_progress = True
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)

    def prompt_play_again(self):
        self.canvas.itemconfig(self.question_text, text="Would you like to play again?")
        self.game_status = GameStatus.PLAY_AGAIN
