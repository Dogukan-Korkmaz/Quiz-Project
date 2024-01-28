class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): .").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print(f"Your current score is :{self.score_up_or_down(True)}/{self.question_number}.")
            print("The answer is correct !")
        else:
            print(f"Your current score is :{self.score_up_or_down(False)}/{self.question_number}.")
            print(f"Correct answer was {correct_answer}.")

    def score_up_or_down(self, con):
        if con:
            self.score += 1
        else:
            self.score -= 1
        return self.score


    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            print(f"Here comes the {self.question_number + 1}. question !")
            return True
        else:
            print("Game is finished !")
            print(f"Your final score is {self.score_up_or_down(None)}.")
            return False
