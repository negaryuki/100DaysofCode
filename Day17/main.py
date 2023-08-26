from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_text = question["text"]
    new_answer = question["answer"]
    new_question = Question(new_text,new_answer)
    question_bank.append(new_question)

# To Do 1 asking Q
# To Do 2 checking if answer was correct
# check if we are at the end of the quiz

quiz = QuizBrain(question_bank)
quiz.next_question()