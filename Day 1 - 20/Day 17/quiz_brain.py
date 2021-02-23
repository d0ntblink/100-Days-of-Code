class QuizBrain:

    def __init__(self, list) -> None:
        self.question_num = 0
        self.question_list = list

    def ask_qestion(self):
        question_obj = self.question_list[self.question_num]
        question = question_obj.question
        answer = question_obj.answer
        if input(f"Q{self.question_num+1}: {question} (true or false?)").lower() == answer.lower():
            pass
        else:
            print("wrong answer, you lose")
            quit()
        self.question_num += 1
        if self.question_num > len(self.question_list)-1:
            print("you won")
            quit()
