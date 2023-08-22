class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Return BOOL to see if the current questin number is not beyond the length of the question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Function that determines the next question to ask and asks for user answer"""
        q_to_ask = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {q_to_ask.text}. (True/False)? ")
        self.check_answer(user_answer, q_to_ask.answer)

    def check_answer(self, user_answer, correct_answer):
        """Function to determine whether the user has answered correctly."""
        # compare the question answer with user answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong :(")
        print(f"The correct_answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        
        # once we reach the ending of the question bank, we want to display the final score
        if self.question_number == len(self.question_list):
            print(f"Your final score is {self.score}/{self.question_number}")
