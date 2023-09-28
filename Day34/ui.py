from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = '#375362'

 
class QuizInterface:
  
  def __init__(self, quiz_brain: QuizBrain):
    
    self.quiz = quiz_brain
#-------------- SETUP WINDOW ---------------
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20,pady=20,bg= THEME_COLOR)
    
#------------------- CANVAS ---------------    
    
    self.canvas = Canvas(width=300, height=250, bg= "white")
    
    self.question_text =self.canvas.create_text(
      150,
      125,
      width= 280,
      text="Question", 
      fill = THEME_COLOR,
      font=("Arial", 20, "italic"
      )     
    self.canvas.grid(row=1,column=0,columnspan = 0, pady =50)
    
#------------------- LABEL  ---------------    
    self.score_label = Label(text="score: 0" , fg ="white" , bg= THEME_COLOR)
    self.score_label.grid(row=0, column=1)
    
  
#------------------- BUTTONS ---------------

    # import pictures:
    cross_img = PhotoImage(file="Images/IMG_0462.png")
    check_img= PhotoImage(file="Images/IMG_0463.png")
    
    # creating buttons:
      
    self.wrong_button= Button(image=cross_img, highlighttickness=0, command = self.false_pressed)
    self.wrong_button.grid(row=2,column=1)
    
    self.right_button= Button(image=check_img, highlighttickness=0, command=self.right_pressed)
    self.right_button.grid(row=2,column=0)
    
    
    self.get_next_question()

    self.window.mainloop()
    
  def get_next_question(self):
    self.canvas.config(bg="white")
    
    if self.quiz.still_has_questions():

      self.score_label.config(text=f"score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text = q_text)
    
    else:
      self.canvas.itemconfig(self.q_text, text = " You have reached the end of the text")
      self.true_button.config(state = "disabled")         self.false_button.config(state = "disabled")  
      
  def right_pressed(self):
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)
  
  
  def false_pressed(self):
    is_right =self.quiz.check_answer("False")
    self.give_feedback(is_right)
    
  def give_feedback(self,is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
        
    self.window.after(100, self.get_next_question)
    
    
