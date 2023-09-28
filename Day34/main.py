from tkinter import *

THEME_COLOR = '#375362'

 
class QuizInterface:
  
  def __init__(self):
    
#-------------- SETUP WINDOW ---------------
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20,pady=20,bg= THEME_COLOR)
    
#------------------- CANVAS ----------------    
    
    self.canvas = Canvas(width=300, height=250, bg= "white")
    
    self.question_text =self.canvas.create_text(
      150,
      125,
      text="Question", 
      fill = THEME_COLOR,
      font=("Arial", 20, "italic"
      )     
    self.canvas.grid(row=1,column=0,columnspan = 0, pady =50)
    
#------------------- LABEL  ---------------    
    
    self.score_label = Label(text="score: 0" , fg ="white" , bg= THEME_COLOR )
    self.score_label.grid(row=0, column=1)
   
#------------------- BUTTONS ---------------

    # import pictures:
    cross_img = PhotoImage(file="Images/IMG_0462.png")
    check_img= PhotoImage(file="Images/IMG_0463.png")
    
    # creating buttons:
      
    self.wrong_button= Button(image=cross_img, highlighttickness=0, command = "no score")
    self.wrong_button.grid(row=2,column=1)
    
    self.right_button= Button(image=check_img, highlighttickness=0, command="plus score")
    self.right_button.grid(row=2,column=0)


    self.window.mainloop()
