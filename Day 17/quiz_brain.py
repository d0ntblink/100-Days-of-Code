class QuizBrain:

    def __init__(self, list) -> None:
        self.question_num = 0
        self.score = 0
        self.question_list = list

    def check_for_question(self):
        return self.question_num < len(self.question_list)

    def ask_qestion(self):
        question_obj = self.question_list[self.question_num]
        question = question_obj.question
        answer = question_obj.answer
        if input(f"Q{self.question_num+1}: {question} (true or false)?: ").lower() == answer.lower():
            print("correct")
            self.score += 1
        else:
            print(f"wrong\nthe correct answer was {answer}")
        self.question_num += 1
        print(f"your current score is {self.score}")
