import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
score = 0
for q in data.question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    question_bank.append(Question(q_text, q_ans))


qb = QuizBrain(question_bank)
while qb.still_has_question:
    if qb.next_question():
        score += 1
    print(f"Your current score is {score}/{qb.question_number}")

