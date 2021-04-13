import random


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def next_question(self):
        i = random.randrange(0, len(self.question_list))
        q = self.question_list[i]
        del self.question_list[i]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {q.text} (True/False):")

        while not (ans.upper() == "TRUE" or ans.upper() == "FALSE"):
            ans = input(f"Q.{self.question_number}: {q.text} (True/False):")

        return self.check_answer(ans, q)

    def check_answer(self, ans, question):
        is_correct = ans.upper() == question.ans.upper()

        if is_correct:
            print(f"You are Right.")
        else:
            print(f"You are Wrong.")

        print(f"The answer was {q.ans}")

        return is_correct

    @property
    def still_has_question(self):
        # return not not self.question_list
        print(len(self.question_list))
        return 0 < len(self.question_list)


