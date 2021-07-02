from data import get_new_questions


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = get_new_questions()
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        # self.check_answer(user_answer)
        return self.current_question.text

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")

    def start_new_game(self):
        self.question_list = get_new_questions()
        self.reset()

    def reset(self):
        self.score = 0
        self.question_number = 0
        self.current_question = None
