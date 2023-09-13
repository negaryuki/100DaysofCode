from tkinter import *
import math

#------------------- CONSTANTS --------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
my_timer= None
#------------------- TIMER RESET ------------------------
def reset_timer():
  window.after_cancel(my_timer)
  canvas.itemconfig(timer_text, text = "00:00")
  title_label.config(text = "Timer")
  check_marks.config(text="")
  
  
#------------------- TIMER MECHANISM ---------------------
def start_timer():
  global reps
  reps += 1
  
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN
  
  if reps % 8 ==0:
    count_down(long_break_sec)
    title_label.config(text="Break", fg= RED)
    
  elif reps % 2 == 0:
    count_down(short_break_sec)
    title_label.config(text = "Break" , fg= PINK)
  
  else:
    count_down(work_sec)
        title_label.config(text= "WORK" , fg= GREEN)
    marks= ""
    work_session = math.floor(reps/2)
       
        for i in range(work_session):
          mark += "✔"
          checkmark_label.config(text=marks, font=(FONT_NAME, 22, "bold"))
  
#------------------ COUNTDOWN MECHANISM ------------------

def count_down(count):
  global my_timer
  
  count_min = math.floor(count/60)    #Returns the largest integer <= X exp. 4.8 = 4
  count_sec = count % 60
  if count_sec <10:
    count_sec= f'0{count_sec}'  
  else:
    start_timer()    # restarts the timer like a for loop
  
  canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}" )    #changing the text of a canvas is different from a label (.config) we have to use ".itemconfig"
  
  if count > 0:
    my_timer=window.after(1000,count_down, count - 1 )  # a method that takes an amount of time that should wait and after that calls a function


#------------------- UI SETUP ----------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#------------------- Canvas Widget ----------------------------  

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # highlightthickness removes the gap between the canvas and window
tomato_img = PhotoImage(file="tomato.png")  # calls the image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)


#------------------- Label ----------------------------  

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)   # fg = foreground which defines the color of the text 

title_label.grid(column=0, row=1)   # Place the label on grid

checkmark_label = Label(fg=GREEN, bg=YELLOW)

checkmark_label.grid(column=1, row=3)   # Place the label on grid

#------------------- Button ----------------------------  

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2, command = start_timer)

reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer
reset_button.grid(column=2, row=2)

window.mainloop()
