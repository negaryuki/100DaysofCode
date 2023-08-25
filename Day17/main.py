from question_model import Question
from data import question_data


question_bank = []

for question in question_data:
    new_text = question["text"]
    new_answer = question["answer"]
    new_question = Question(new_text,new_answer)
    question_bank.append(new_question)
