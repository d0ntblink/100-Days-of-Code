from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for enteries in question_data:
    enteries = Question(question=enteries["text"], answer=enteries["answer"])
    question_bank.append(enteries)

quiz = QuizBrain(list=question_bank)

while True:
    quiz.ask_qestion()
