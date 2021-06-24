from questions_fetcher import QuestionsFetcher
from question_model import Question

question_data = QuestionsFetcher.prepare_10_questions()


def get_new_questions() -> list:
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank

# question_data = [
#     {
#         "category": "Entertainment: Film",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The film \"2001: A Space Odyssey\" was released on December 31st, 2000.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Entertainment: Film",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The word \"Inception\" came from the 2010 blockbuster hit \"Inception\".",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Entertainment: Video Games",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "In the video game \"Transistor\", \"Red\" is the name of the main character.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Entertainment: Music",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Scatman John's real name was John Paul Larkin.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Entertainment: Video Games",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "\"Return to Castle Wolfenstein\" was the only game of the Wolfenstein series where you don't play as William \"B.J.\" Blazkowicz.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Entertainment: Japanese Anime & Manga",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In Chobits, Hideki found Chii in his apartment.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Geography",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "There is an island in Japan called \u014ckunoshima, A.K.A. \"Rabbit Island\", so named because of it's huge population of rabbits.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The T-Mobile Sidekick smartphone is a re-branded version of the Danger Hiptop.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Entertainment: Video Games",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "In \"Resident Evil\", only Chris has access to the grenade launcher.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]