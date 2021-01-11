from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print(question_bank[0].text)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print(f"You have completed the quiz\nYour final score is: {new_quiz.score}/{new_quiz.question_number}")
