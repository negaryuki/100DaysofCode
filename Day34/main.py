from tkinter import *

THEME_COLOR = '#375362'

 
class QuizInterface:
  
  def __init__(self):
    
#-------------- SETUP WINDOW ---------------
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20,pady=20,bg= THEME_COLOR)
    
#------------------- CANVAS ---------------    
    
    self.canvas = Canvas(width=300, height=250)
    self.canvas, 
    
    self.canvas = Canvas(width=800, height=526)
    self.canvas_text =canvas.create_text(400,150, text="Question", font=("Arial", 20, "italic")) 
    self.canvas.config(bg= "white", highlighttickness=0)
    self.canvas.grid(row=0,column=0)

#------------------- BUTTONS ---------------

    # import pictures:
    cross_img = PhotoImage(file="Images/IMG_0462.png")
    check_img= PhotoImage(file="Images/IMG_0463.png")
    
    # creating buttons:
      
    self.wrong_button= Button(image=cross_img, highlighttickness=0, command = "no score")
    self.wrong_button.grid(row=2,column=0)
    
    self.right_button= Button(image=check_img, highlighttickness=0, command="plus score")
    self.right_button.grid(row=2,column=1)


    self.window.mainloop()
