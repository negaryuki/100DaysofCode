# create a class called QuizBrain

# Write an __init__() method
# initialize the question_number to 0
# initialize the question_list to an input

from question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f" Q.{self.question_number}: {current_question.text} (True\False) : ")
