from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_text = question["question"]
    new_answer = question["correct_answer"]
    new_question = Question(new_text,new_answer)
    question_bank.append(new_question)

# To Do 1 asking Q
# To Do 2 checking if answer was correct
# check if we are at the end of the quiz

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f' You have completed the Game! Your final score is {quiz.score} {len(question_bank)}')