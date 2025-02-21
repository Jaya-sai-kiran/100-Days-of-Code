class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q{self.question_number}:{q.text}(True/False):\n")
        self.check_answer(user_answer,q.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("Wrong answer")
            print("The correct answer was:",correct_answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def the_end(self):
        print("You've completed the quiz")
        print(f"Your final score was:{self.score}/{self.question_number}")