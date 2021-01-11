class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        correct_input = False
        while not correct_input:
            reply = input(f"Q.{self.question_number}: {current_question.text} (True or False?): ")
            if reply.lower() in ("true", "false"):
                correct_input = True
            else:
                print("Check your input.")
        self.__check_answer(reply, current_question.answer)

    def __check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}\nYour current score: {self.score}/{self.question_number}\n")

